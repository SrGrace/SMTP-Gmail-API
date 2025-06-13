# 📧 Gmail SMTP Email Sender

This project allows you to send emails using Python via Gmail's SMTP server. It uses a secure app password for authentication.

## 🔐 Gmail Configuration (One-Time Setup)

To use Gmail's SMTP server, follow these steps to generate an app password:

### 1. Enable 2-Step Verification

- Visit: [https://myaccount.google.com/security](https://myaccount.google.com/security)
- Scroll down to **"Signing in to Google"**
- Enable **2-Step Verification** and complete the setup

### 2. Generate App Password

- Go to: [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
- Select **Mail** as the app and **Other** or your device name
- Click **Generate**
- **Copy the 16-character app password** — you'll use this instead of your Gmail account password

## 🛠️ Project Setup

### Prerequisites

- `Python 3.x`
- `fastapi`
- `uvicorn`
- `pydantic`
- `smtplib` and `email` (standard libraries)

### Run
- `python app.py`
