from config import EMAIL_ADRESS, EMAIL_PASS
import smtplib

class sendInfo(object):
    """Send the advisors advice"""

    def __init__(self, email, msg):
        """Constructor"""
        self.email = email
        self.msg = msg

    def sendIt(self):
        """Sending the email"""
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(user=EMAIL_ADRESS, password=EMAIL_PASS)

            subject = 'Your stock advice'
            body = self.msg
            email = f'subject:{subject}\n\n{body}'

            smtp.sendmail(from_addr=EMAIL_ADRESS, to_addrs=self.email, msg=email)
