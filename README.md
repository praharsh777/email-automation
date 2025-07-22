# 📧 Email Automation for HR Outreach

This project automates sending personalized internship/job inquiry emails to HR professionals using Gmail.  
It reads data from a CSV file, sends **one email per run** (with an attached resume), and marks each sent contact to avoid duplication.

---

## 🚀 Features

- ✅ Sends **1 email per script run** (ideal for GitHub Actions or cron scheduling)
- ✅ Skips rows already marked as `Sent`
- ✅ Attaches resume PDF automatically
- ✅ Reads Gmail credentials securely via **GitHub Secrets**
- ✅ Gracefully handles malformed CSV rows
- ✅ Skips top 5 rows if you manually contacted them

---

## 📂 Project Structure

├── send_emails.py # Main Python script
├── resume.pdf # Your resume to attach
├── hr_contacts.csv # CSV file with HR data
├── .github/
│ └── workflows/
│ └── email_sender.yml # GitHub Actions workflow (auto-scheduler)
├── .gitignore # Ensures secrets and cache aren't pushed
└── README.md # This file

---

## 📄 CSV Format

The CSV must have the following columns:

SNo, Name, Email, Title, Company, [Other], Status



- `Status` column is used to track who already received emails.
- Script automatically creates `Status` if not present.
- Example:

SNo,Name,Email,Title,Company,Status
1,John Doe,john@example.com,HR Head,Acme Corp,
🔐 Secrets & Environment Setup
No .env file is needed when using GitHub Actions.
Instead, go to your GitHub repo:

Settings → Secrets → Actions, and add:

SENDER_EMAIL → your Gmail (e.g. praharshsai46@gmail.com)

APP_PASSWORD → your Gmail App Password (NOT your login password)
👉 Learn how to get App Password

💌 Manual Usage
If running locally (optional):

python send_emails.py

Each run sends only 1 email, marks that row as Sent, and saves the CSV.

⏰ Automated Scheduling (Recommended)
We recommend GitHub Actions for automation.

Sends 1 email every 15 minutes

Stays well under Gmail’s 100–150/day safe limit

You can also host using:

 PythonAnywhere

 Google Cloud Scheduler

 Render.com (free tier limited)

🛠 GitHub Actions Workflow
GitHub automatically runs your script every 15 minutes via this workflow:

.github/workflows/email_sender.yml

name: Send 1 Email Every 15 Minutes

on:
  schedule:
    - cron: "*/15 * * * *"
  workflow_dispatch:

jobs:
  send_email:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repo
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          pip install pandas

      - name: Run email script
        env:
          SENDER_EMAIL: ${{ secrets.SENDER_EMAIL }}
          APP_PASSWORD: ${{ secrets.APP_PASSWORD }}
        run: |
          python send_emails.py
🔐 Security Tips
Use GitHub Secrets to hide credentials

Never commit .env or credentials

Keep your repo private if it contains real email data

🙌 Credits
Created by: Praharsh Sai
📧 Email: praharshsai867@gmail.com
🔗 LinkedIn:[ M Praharsh Sai]([url](https://www.linkedin.com/in/m-praharsh-sai-77b1ab275/))
