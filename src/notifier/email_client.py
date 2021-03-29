class EmailNotifier:
    from config.config import Config

    def __init__(self, config: Config):
        import smtplib
        import ssl
        smtp_server = config.get_smtp_server_host()
        port = config.get_smtp_port()  # For SSL
        password = config.get_smtp_password()

        self._sender_email = config.get_smtp_sender()
        self._recipients = config.get_email_recipient_list()

        self._server = smtplib.SMTP_SSL(smtp_server, port, context=ssl.create_default_context())
        self._server.login(self._sender_email, password)

    def send_email(self):
        message = """\
                Subject: Mailbox alert
                New mail alert"""

        for recipient in self._recipients:
            self._server.sendmail(self._sender_email,recipient, message)
