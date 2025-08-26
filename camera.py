import streamlit as st
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

st.set_page_config(page_title="Email Sender", page_icon="📧")
st.title("📧 Send Email via Gmail (SMTP)")

# Load credentials from secrets.toml
sender_email = st.secrets["gmail"]["sender_email"]
password = st.secrets["gmail"]["app_password"]

# Email form
receiver_email = st.text_input("Recipient Email", "@gmail.com")
subject = st.text_input("Subject")
body = st.text_area("Message")

if st.button("Send Email"):
    if receiver_email and subject and body:
        try:
            # Create email message
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            # SMTP connection
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            server.quit()

            st.success("✅ Email sent successfully!")
        except Exception as e:
            st.error(f"❌ Failed to send email: {e}")
    else:
        st.warning("⚠️ Please fill in all fields.")
