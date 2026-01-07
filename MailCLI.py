
import pyfiglet

# Print MAILCLI banner once
print(pyfiglet.figlet_format("MAILCLI", font="slant"))


import smtplib
import logging
from email.message import EmailMessage
from datetime import datetime



LOG_FILE = "mailer.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

logging.info("Program started")


def send_email(sender, app_password, receiver, subject, body):
    """
    Sends an email using Gmail SMTP with TLS and App Password (2FA)
    """

    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = receiver

    try:
        logging.info("Connecting to SMTP server")

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  # Secure the connection

        logging.info("Logging in to SMTP server")
        server.login(sender, app_password)

        logging.info("Sending email")
        server.send_message(msg)

        server.quit()

        logging.info("Email sent successfully")
        print("\n Email sent successfully!")

    except smtplib.SMTPAuthenticationError:
        logging.error("Authentication failed (wrong App Password)")
        print("\n Authentication failed")
        print(" Check your App Password (NOT normal Gmail password)")

    except Exception as e:
        logging.exception("Unexpected error occurred")
        print("\n Failed to send email")
        print("Error:", e)



def main():
    print("MailCLI SMTP")
    print("-----------------------------------")

    sender_email = input("Gmail address: ").strip()
    app_password = input("Gmail App Password (16 chars): ").strip()
    receiver_email = input("Receiver email: ").strip()
    subject = input("Subject: ").strip()
    body = input("Message body: ").strip()

    logging.info(f"Email request | From: {sender_email} | To: {receiver_email}")

    send_email(
        sender=sender_email,
        app_password=app_password,
        receiver=receiver_email,
        subject=subject,
        body=body
    )

    logging.info("Program finished")


if __name__ == "__main__":
    main()
