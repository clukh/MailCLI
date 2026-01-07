<<<<<<< HEAD
=======

import pyfiglet


print(pyfiglet.figlet_format("MAILCLI", font="slant"))


>>>>>>> 6e450347e15fb11112167cadeff8645a1e08b94d
import smtplib
import ssl
import os
import sys
import time
import logging
import threading
from email.message import EmailMessage

# =========================
# PATHS & LOGGING
# =========================

BASE_DIR = os.path.dirname(sys.executable if getattr(sys, "frozen", False) else os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "mailer.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler()
    ]
)

# =========================
# ASCII TITLE (SAFE)
# =========================

def banner():
    print(r"""
  __  __       _ _  ____ _     ___ 
 |  \/  | __ _(_) |/ ___| |   |_ _|
 | |\/| |/ _` | | | |   | |    | | 
 | |  | | (_| | | | |___| |___ | | 
 |_|  |_|\__,_|_|_|\____|_____|___|

           SMTP Console Mailer
""")
print("        v1.5 • by clukh\n")


# =========================
# MASKED PASSWORD INPUT
# =========================

def masked_input(prompt, timeout=60):
    import msvcrt

    print(prompt, end="", flush=True)
    password = ""
    start_time = time.time()

<<<<<<< HEAD
    while True:
        if time.time() - start_time > timeout:
            raise TimeoutError("Password input timed out")
=======
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  
>>>>>>> 6e450347e15fb11112167cadeff8645a1e08b94d

        if msvcrt.kbhit():
            char = msvcrt.getch()

            if char in {b"\r", b"\n"}:
                print()
                return password

            elif char == b"\x08":  # Backspace
                if password:
                    password = password[:-1]
                    print("\b \b", end="", flush=True)

            elif char == b"\x03":
                raise KeyboardInterrupt

            else:
                password += char.decode(errors="ignore")
                print("*", end="", flush=True)

        time.sleep(0.01)

# =========================
# TIMED INPUT (NON-PASSWORD)
# =========================

def timed_input(prompt, timeout=60):
    result = [None]

    def worker():
        result[0] = input(prompt)

    thread = threading.Thread(target=worker)
    thread.daemon = True
    thread.start()
    thread.join(timeout)

    if thread.is_alive():
        raise TimeoutError("Input timed out")

    return result[0]

# =========================
# SMTP PROVIDERS
# =========================

SMTP_PROVIDERS = {
    "gmail": ("smtp.gmail.com", 587),
    "outlook": ("smtp.office365.com", 587),
    "yahoo": ("smtp.mail.yahoo.com", 587),
}

# =========================
# MAIN PROGRAM
# =========================

def main():
    logging.info("Program started")
    banner()

    try:
        provider = timed_input("SMTP Provider (gmail/outlook/yahoo/custom): ", 30).strip().lower()

        if provider == "custom":
            host = timed_input("SMTP Host: ", 30).strip()
            port = int(timed_input("SMTP Port: ", 30))
        elif provider in SMTP_PROVIDERS:
            host, port = SMTP_PROVIDERS[provider]
        else:
            print("❌ Invalid provider")
            return

        sender = timed_input("Your email address: ", 30).strip()
        password = masked_input("App Password (masked): ", timeout=60)
        receiver = timed_input("Receiver email: ", 30).strip()
        subject = timed_input("Subject: ", 60)
        body = timed_input("Message body: ", 120)

        msg = EmailMessage()
        msg["From"] = sender
        msg["To"] = receiver
        msg["Subject"] = subject
        msg.set_content(body)

        # Attachments
        attach = timed_input("Add attachment? (y/n): ", 20).lower()
        while attach == "y":
            path = timed_input("Attachment file path: ", 60).strip()
            if os.path.isfile(path):
                with open(path, "rb") as f:
                    data = f.read()
                filename = os.path.basename(path)
                msg.add_attachment(data, maintype="application", subtype="octet-stream", filename=filename)
                logging.info(f"Attachment added: {filename}")
            else:
                print("❌ File not found")

            attach = timed_input("Add another attachment? (y/n): ", 20).lower()

        logging.info(f"Connecting to {host}:{port}")

        context = ssl.create_default_context()
        with smtplib.SMTP(host, port, timeout=30) as server:
            server.starttls(context=context)
            server.login(sender, password)
            server.send_message(msg)

        print("✅ Email sent successfully")
        logging.info("Email sent successfully")

    except TimeoutError as e:
        print(f"⏱️ Timeout: {e}")
        logging.error(str(e))

    except smtplib.SMTPAuthenticationError:
        print("❌ Authentication failed (wrong App Password)")
        logging.error("SMTP authentication failed")

    except KeyboardInterrupt:
        print("\n❌ Cancelled by user")
        logging.warning("User cancelled program")

    except Exception as e:
        print(f"❌ Error: {e}")
        logging.exception("Unhandled exception")

    finally:
        logging.info("Program finished")

# =========================
# ENTRY POINT
# =========================

if __name__ == "__main__":
    main()
