import smtplib
from email.mime.text import MIMEText

msg = MIMEText("The body of the email is here")

msg['Subject'] = "An Email Alert"
msg['From'] = "report@mediage.co.kr"
msg['To'] = "skc3779@mediage.co.kr"

s = smtplib.SMTP('118.128.208.148', 25)
s.login("support@mediage.co.kr", "support1234~~")
s.send_message(msg)
s.quit()