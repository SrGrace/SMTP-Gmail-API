import os
import smtplib
from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import uvicorn

from dotenv import load_dotenv
load_dotenv(override=True)

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")

app = FastAPI("SMTP Gmail APP")

class EmailRequest(BaseModel):
    to: str
    subject: str
    body: str

@app.post("/send_email")
def send_email(request: EmailRequest):
    try:
        to = request.to
        subject = request.subject
        body = request.body

        user_msg = MIMEMultipart()
        user_msg["From"] = SENDER_EMAIL
        user_msg["To"] = to
        user_msg["Subject"] = subject
        user_msg.attach(MIMEText(body, "plain"))

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, [to], user_msg.as_string())

        # Return void response (204 No Content)
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to send email: {str(e)}"
        )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
