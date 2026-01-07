#  MAILCLI

MAILCLI is a **professional console-based SMTP email sender** written in Python.  
Designed for **learning, automation, and legitimate email notifications**.

> Supports Gmail SMTP  
> Uses **2FA (App Passwords)**  
> Includes **logging system**  
> Beginner-friendly & production-style code  
> Portfolio-ready project

---

##  Features

- Send emails via **Gmail SMTP**
- Secure connection using **TLS**
- **2FA compliant** (App Password, not normal password)
- Detailed **logging to file and console**
- Clean error handling
- Runs fully in the **terminal / console**
- Prints **MAILCLI banner** on start

---

##  How SMTP Works 

- SMTP = Internet postman 
- Your Python script writes a letter (email)  
- Gmail SMTP delivers it securely  
- This project **only sends emails**, it does **not read inbox**  

---

##  Requirements

- Python **3.8+** (tested on 3.11/3.12)  
- A Gmail account  
- **2-Step Verification (2FA) enabled**  
- Gmail **App Password**  

---

##  Enable 2FA & App Password (Required)

### Step 1: Enable 2FA
1. Go to **Google Account → Security**  
2. Enable **2-Step Verification**  

### Step 2: Generate App Password
1. Google Account → Security → **App passwords**  
2. App: `Mail`  
3. Device: `Other (Python)`  
4. Click **Generate** → copy the **16-character password**  
5. **Remove any spaces** when entering in Python  

>  This is **NOT** your normal Gmail password  

---

##  How to Run

1. Clone or download this repository  
2. Open a terminal in the project folder  
3. Run:

### Example usage 
 
  __  __    _    _ _      ____ _     ___ 
|  \/  |  / \  | | |    / ___| |   |_ _|
| |\/| | / _ \ | | |   | |   | |    | | 
| |  | |/ ___ \| | |___| |___| |___ | | 
|_|  |_/_/   \_\_|_____\____|_____|___|

📧 SMTP Console Mailer (Professional)
-----------------------------------
Gmail address: abc@gmail.com
Gmail App Password (16 chars, NO SPACES): abcdefghijklmnop
Receiver email: xyz@gmail.com
Subject: Test Email
Message body: Hello from MAILCLI!

✅ Email sent successfully!

```bash
python MAILCLI.py