import smtplib
from smtplib import SMTP
from email.message import EmailMessage
def sendmail(email,body,subject):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('balaradhakrishna34@gmail.com','gnbg ykuu sufd yrvv')
    msg=EmailMessage()
    msg['FROM']='balaradhakrishna34@gmail.com'
    msg['TO']=email
    msg['SUBJECT']=subject
    msg.set_content(body)
    server.send_message(msg)
    server.quit()