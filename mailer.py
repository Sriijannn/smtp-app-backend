import smtplib
from email.mime.text import MIMEText
from typing import List, Tuple

def send_email(sender_email: str, app_password: str, recipient_email: str, subject: str, body: str) -> Tuple[str, str]:
    try:
        msg = MIMEText(body, "plain")
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = recipient_email

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, app_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())

        return recipient_email, "success"
    except Exception as e:
        return recipient_email, "error"
