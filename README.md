# Email Inbox Address Counter

This Python script connects to your email account via IMAP, extracts sender email addresses from all emails in your inbox, counts the number of emails per sender, and exports the results to a text file. It includes a progress bar to track processing.

## Features
- Connects to Gmail (or other IMAP-supported email providers).
- Counts emails by sender address.
- Displays a progress bar using `tqdm`.
- Exports results to `email_counts.txt`.

## Prerequisites
- Python 3.12.10 or higher.
- An email account with IMAP enabled and an app password (if 2FA is enabled).

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/lee-har/inbox-addressor.git
   cd email-address-counter
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Enable IMAP in Gmail:
   - Go to [Gmail Settings](https://mail.google.com/) > **See all settings** > **Forwarding and POP/IMAP** > Enable IMAP.
4. Generate an app password (if 2FA is enabled):
   - Go to [Google Account Security](https://myaccount.google.com/security) > **App passwords**.
   - Select **Mail** and **Windows Computer**, then generate and copy the password.

## Usage
1. Update the script with your credentials:
   Edit `email_address_counter.py` and replace:
   ```python
   EMAIL_ADDRESS = "your_email@gmail.com"
   APP_PASSWORD = "your_app_password"
   ```
   with your Gmail address and app password.
2. Run the script:
   ```bash
   python email_address_counter.py
   ```
3. Check the output:
   - The script will process emails and show a progress bar.
   - Results are saved to `email_counts.txt` in the format:
     ```
     Email Address Counts
     ====================
     sender1@example.com: 25 emails
     sender2@example.com: 10 emails
     ...
     ```

## Configuration
- To use a different email provider, update `imap_server` in `connect_to_email` (e.g., `imap-mail.outlook.com` for Outlook).
- To process a different folder, change `folder` in `extract_email_addresses` (default is `"INBOX"`).

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
