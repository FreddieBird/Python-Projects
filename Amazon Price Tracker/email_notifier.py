import smtplib


class EmailNotifier(object):
    """
    Simple class for sending email notifications.
    """

    def __init__(self, email_address, email_pass, smtp_address):
        self.email_address = email_address
        self.email_pass = email_pass
        self.smtp_address = smtp_address

    def send_email(self, send_address, message):
        """
        Creates a connection and sends email containing message.

        Parameters
        ----------
        send_address : `str`
            Email address to send to.
        message :  `str`
            Message to be emailed.
        """
        with smtplib.SMTP(self.smtp_address, port=587) as connection:
            connection.starttls()
            result = connection.login(self.email_address, self.email_pass)
            connection.sendmail(
                from_addr=self.email_address,
                to_addrs=send_address,
                msg=message
            )
