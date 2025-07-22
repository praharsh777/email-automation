import os
import pandas as pd
import smtplib
from email.message import EmailMessage

# ========== CONFIG ==========
SENDER_EMAIL = os.getenv('SENDER_EMAIL')
APP_PASSWORD = os.getenv('APP_PASSWORD')
RESUME_PATH = 'resume.pdf'
CSV_FILE = 'hr_contacts.csv'
LINKEDIN_URL = 'https://www.linkedin.com/in/m-praharsh-sai-77b1ab275/'
# ============================

# Safety check for environment variables
if not SENDER_EMAIL or not APP_PASSWORD:
    print("[✗] Missing email credentials. Check GitHub environment secrets.")
    exit()

# Load CSV and handle errors gracefully
try:
    df = pd.read_csv(CSV_FILE, engine='python', on_bad_lines='skip')
    df.columns = df.columns.str.strip()
    if 'Status' not in df.columns:
        df['Status'] = ''
except Exception as e:
    print(f"[✗] Failed to read CSV file: {e}")
    exit()

# Generate email body content
def create_email_body(name, company):
    return f"""Hi {name},

I hope you're doing well. My name is Praharsh Sai, and I’m currently in my 4th year of B.Tech, specializing in Computer Science and Engineering with a focus on Data Science.

I’m reaching out to express my interest in any internship or job opportunities within {company}. I'm particularly eager to learn more about your upcoming projects, the challenges your team is tackling, and the innovation you're driving—especially in areas involving AI, automation, or product development.

With a passion for full-stack development and AI/ML, I'm enthusiastic about contributing to impactful, real-world solutions and supporting your mission at {company}.

I’ve attached my resume for your reference. You can also view my LinkedIn profile here: {LINKEDIN_URL}

Looking forward to the opportunity to connect.

Best regards,  
Praharsh Sai  
praharshsai867@gmail.com
"""

# Build the email object
def compose_email(name, email, company):
    msg = EmailMessage()
    msg['Subject'] = f"Interest in Internship/Job Opportunities at {company}"
    msg['From'] = SENDER_EMAIL
    msg['To'] = email
    msg.set_content(create_email_body(name, company))

    with open(RESUME_PATH, 'rb') as f:
        msg.add_attachment(f.read(), maintype='application', subtype='pdf', filename='Praharsh_Sai_Resume.pdf')
    return msg

# Main function to send one email per run
def main():
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(SENDER_EMAIL, APP_PASSWORD)

        for index, row in df.iterrows():
            if index < 5:
                continue  # Skip top 5 (already sent manually)

            status = str(row.get('Status', '')).strip().lower()
            if status == 'sent':
                continue

            name = str(row.get('Name', '')).strip()
            email = str(row.get('Email', '')).strip()
            company = str(row.get('Company', '')).strip()

            if not name or not email or not company:
                continue  # Skip incomplete rows

            try:
                msg = compose_email(name, email, company)
                smtp.send_message(msg)
                print(f"[✓] Email sent to {name} at {company} ({email})")

                # Update CSV and mark this contact as 'Sent'
                df.at[index, 'Status'] = 'Sent'
                df.to_csv(CSV_FILE, index=False)
                break  # Only send 1 email per run
            except Exception as e:
                print(f"[✗] Failed to send email to {email}: {e}")
                continue

if __name__ == '__main__':
    main()
