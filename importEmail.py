import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

def send_email(subject, body, to_email):
    # Email account credentials
    from_email = "your_email@example.com"
    password = "your_password"
    
    # Create a MIMEMultipart object
    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = subject
    
    # Add body to the email
    message.attach(MIMEText(body, 'plain'))
    
    # Establish a secure session with the SMTP server
    server = smtplib.SMTP('smtp.example.com', 587)  # Use your SMTP server details
    server.starttls()
    server.login(from_email, password)
    
    # Send the email and close the server connection
    server.send_message(message)
    server.quit()

# Set up the email content
subject = "Daily Report for " + datetime.datetime.now().strftime("%Y-%m-%d")
body = "Here is your daily report..."
to_email = "recipient@example.com"

send_email(subject, body, to_email)
