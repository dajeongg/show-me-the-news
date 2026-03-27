from config import SMTP_EMAIL, SMTP_PASSWORD, TO_EMAILS
import smtplib
from email.mime.text import MIMEText

def send_email(subject, html_body):
    msg = MIMEText(html_body, "html")
    msg["Subject"] = subject
    msg["From"] = SMTP_EMAIL
    
    # 👉 To에는 자기 자신 (형식용)
    msg["To"] = SMTP_EMAIL
    
    # 👉 BCC로 실제 수신자들 숨김 처리
    msg["Bcc"] = ", ".join(TO_EMAILS)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SMTP_EMAIL, SMTP_PASSWORD)
        server.send_message(msg)
