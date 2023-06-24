import smtplib
import datetime
# from email.mime import *

# Set up the email message
msg = "Hello, this email was sent after three days."
subj= 'Email after Three Days'
fro = 'kharrylungu@gmail.com'
tt = 'sheilasharon10@gmail.com'

# Set the date to three days from now
now = datetime.datetime.now()
send_date = now + datetime.timedelta(days=3)
send_date_str = send_date.strftime('%a, %d %b %Y %H:%M:%S %z')

# Connect to the SMTP server
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'imutkupc@gmail.com'
smtp_password = 'lynnmutuku254'
smtp_conn = smtplib.SMTP(smtp_server, smtp_port)
smtp_conn.ehlo()
smtp_conn.starttls()
smtp_conn.login(smtp_username, smtp_password)

# Send the email
smtp_conn.sendmail(fro, tt, msg.as_string(), mail_options=['Date: ' + send_date_str])
smtp_conn.quit()
