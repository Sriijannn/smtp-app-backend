from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
import os
from email.mime.text import MIMEText

app = Flask(__name__)
CORS(app, origins=["https://smtp-mailer-app-1.onrender.com"])

@app.route("/send-emails", methods=["POST"])
def send_emails():
    data = request.get_json()

    # Use camelCase keys as sent from frontend
    gmail_user = data.get("gmail_user")
    app_password = data.get("gmail_app_password")
    to_email = data.get("to_email")
    subject = data.get("subject")
    body = data.get("content")

    if not all([gmail_user, app_password, to_email, subject, body]):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = gmail_user
        msg["To"] = to_email

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(gmail_user, app_password)
            server.sendmail(gmail_user, to_email, msg.as_string())

        return jsonify({"results": [{"email": to_email, "status": "success"}]})
    except Exception as e:
        return jsonify({"results": [{"email": to_email, "status": "error", "error": str(e)}]}), 500


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

