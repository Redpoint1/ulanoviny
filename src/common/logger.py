import datetime
import logging
import logging.handlers
import os

__all__ = ('LOGGER', 'DEFAULT_FORMAT')

DEFAULT_FORMAT = logging.Formatter('%(levelname)s: %(message)s')


class BufferingSMTPHandler(logging.handlers.BufferingHandler):
    def __init__(self, mailhost, fromaddr, toaddrs, subject,
                 credentials=None, secure=None, timeout=5.0, capacity=1000):
        logging.handlers.BufferingHandler.__init__(self, capacity)
        if isinstance(mailhost, (list, tuple)):
            self.mailhost, self.mailport = mailhost
        else:
            self.mailhost, self.mailport = mailhost, None
        if isinstance(credentials, (list, tuple)):
            self.username, self.password = credentials
        else:
            self.username = None
        self.fromaddr = fromaddr
        if isinstance(toaddrs, str):
            toaddrs = [toaddrs]
        self.toaddrs = toaddrs
        self.subject = subject
        self.secure = secure
        self.timeout = timeout
        self.max_level = 0

    def emit(self, record):
        if record.levelno > self.max_level:
            self.max_level = record.levelno
        super(BufferingSMTPHandler, self).emit(record)

    @property
    def max_level_name(self):
        return logging.getLevelName(self.max_level)

    @staticmethod
    def timestamp():
        return datetime.datetime.now().astimezone().isoformat(sep=' ', timespec='seconds')

    def flush(self):
        self.acquire()
        try:
            if len(self.buffer) > 0:
                import smtplib
                from email.message import EmailMessage
                import email.utils

                port = self.mailport
                if not port:
                    port = smtplib.SMTP_PORT
                smtp = smtplib.SMTP(self.mailhost, port, timeout=self.timeout)
                msg = EmailMessage()
                msg['From'] = self.fromaddr
                msg['To'] = ','.join(self.toaddrs)
                msg['Subject'] = f'[{self.max_level_name}] {self.subject} from {self.timestamp()}'
                msg['Date'] = email.utils.localtime()
                content = ''
                for record in self.buffer:
                    s = self.format(record)
                    content = content + s + "\r\n"
                msg.set_content(content)
                if self.username:
                    if self.secure is not None:
                        smtp.ehlo()
                        smtp.starttls(*self.secure)
                        smtp.ehlo()
                    smtp.login(self.username, self.password)
                smtp.send_message(msg)
                smtp.quit()
            self.buffer = []
        except Exception as e:
            raise e
        finally:
            self.release()


LOGGER = logging.getLogger(__name__)
handler = logging.StreamHandler()
mail_handler = BufferingSMTPHandler(
    mailhost=(os.environ.get('SMTP_HOST'), os.environ.get('SMTP_PORT')),
    fromaddr=os.environ.get('SMTP_FROM'),
    toaddrs=[os.environ.get('SMTP_TO')],
    subject=os.environ.get('SMTP_SUBJECT'),
    credentials=(os.environ.get('SMTP_MAIL'), os.environ.get('SMTP_PASS')),
    secure=()
)
mail_handler.setFormatter(DEFAULT_FORMAT)
handler.setFormatter(DEFAULT_FORMAT)
LOGGER.addHandler(handler)
LOGGER.addHandler(mail_handler)
LOGGER.setLevel(logging.INFO)
