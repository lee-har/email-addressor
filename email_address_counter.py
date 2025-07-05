import imaplib
import email
from email.header import decode_header
from collections import Counter
import re
import os
from tqdm import tqdm

def connect_to_email(email_address, app_password, imap_server="imap.gmail.com"):
    """Connect to the email server using IMAP."""
    try:
        imap = imaplib.IMAP4_SSL(imap_server)
        imap.login(email_address, app_password)
        return imap
    except Exception as e:
        print(f"Error connecting to email server: {e}")
        return None

def decode_email_subject(subject):
    """Decode email subject line."""
    decoded_subject = decode_header(subject)[0][0]
    if isinstance(decoded_subject, bytes):
        try:
            return decoded_subject.decode()
        except:
            return decoded_subject.decode('utf-8', errors='ignore')
    return decoded_subject

def extract_email_addresses(imap, folder="INBOX"):
    """Extract sender email addresses from all emails in the specified folder."""
    try:
        imap.select(folder)
        _, message_numbers = imap.search(None, "ALL")
        email_counts = Counter()
        total_emails = len(message_numbers[0].split())

        # Initialize progress bar
        with tqdm(total=total_emails, desc="Processing emails", unit="email") as pbar:
            for num in message_numbers[0].split():
                _, msg_data = imap.fetch(num, "(RFC822)")
                email_message = email.message_from_bytes(msg_data[0][1])
                
                # Extract sender
                from_header = email_message.get("From")
                if from_header:
                    # Use regex to extract email address from From header
                    email_match = re.search(r'<(.+?)>', from_header) or re.search(r'(\S+@\S+\.\S+)', from_header)
                    if email_match:
                        sender_email = email_match.group(1)
                        email_counts[sender_email] += 1
                
                # Update progress bar
                pbar.update(1)

        return email_counts
    except Exception as e:
        print(f"Error processing emails: {e}")
        return Counter()

def export_to_txt(email_counts, output_file="email_counts.txt"):
    """Export email address counts to a text file."""
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("Email Address Counts\n")
            f.write("====================\n\n")
            for email, count in email_counts.most_common():
                f.write(f"{email}: {count} emails\n")
        print(f"Results exported to {output_file}")
    except Exception as e:
        print(f"Error exporting to file: {e}")

def main():
    # Replace with your email and app password
    EMAIL_ADDRESS = "ENTER_EMAIL_ADDRESS"
    APP_PASSWORD = "ENTER_APP_PASSWORD"
    OUTPUT_FILE = "email_counts.txt"

    # Connect to email server
    imap = connect_to_email(EMAIL_ADDRESS, APP_PASSWORD)
    if not imap:
        return

    # Extract and count email addresses
    email_counts = extract_email_addresses(imap)
    
    # Export results to text file
    if email_counts:
        export_to_txt(email_counts, OUTPUT_FILE)
    
    # Logout and close connection
    imap.logout()

if __name__ == "__main__":
    main()