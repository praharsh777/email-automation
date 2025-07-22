# 📧 Email Automation for HR Outreach

This project automates sending personalized internship/job inquiry emails to HR professionals using Gmail.  
It reads data from a CSV file, sends **one email per run** (with an attached resume), and marks each sent contact to avoid duplication.

---

## 🚀 Features

- ✅ Sends **1 email per script run** (ideal for scheduling)
- ✅ Skips rows already marked as `Sent`
- ✅ Attaches resume PDF automatically
- ✅ Loads environment variables from `.env` file for security
- ✅ Gracefully handles malformed CSV rows

---

## 📂 Project Structure

├── send_emails.py # Main Python script
├── resume.pdf # Your resume to attach
├── hr_contacts.csv # CSV file with HR data
├── .env # Environment variables (not committed)
├── .gitignore # Ensures .env and cache aren't pushed
└── README.md # This file

---

## 📄 CSV Format

The CSV must have the following columns:
SNo, Name, Email, Title, Company, [Other], Status


- `Status` should be blank or "Sent"
- Script automatically appends `Status` if missing
- Example:

```csv
SNo,Name,Email,Title,Company,Status
1,John Doe,john@example.com,HR Head,Acme Corp,
```

## 🔐 Environment Variables
Create a .env file in the project root:

## ⚠️ Use a Gmail App Password (not your Gmail login password).
Learn more: https://support.google.com/mail/answer/185833

## 💌 Usage
Run the script using Python:

python send_emails.py

## ⏰ Scheduling (Recommended)
To send 80–100 emails per day, host and schedule using:

GitHub Actions

Render Cron Jobs

PythonAnywhere

Google Cloud Scheduler

We'll send one email per 15 minutes to stay within Gmail's sending limits.

## 🔐 Security Tips
Always use .env and .gitignore to avoid exposing credentials.

Keep this repo private unless you're sharing it without real data.

## 🙌 Credits
Created by Praharsh Sai
Email:
📫 praharshsai867@gmail.com
