from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.conf import settings


class SendMail(object):

    @staticmethod
    def send_no_reply_email(to_emails, subject, content):

        message = Mail(from_email='no_reply@welldone.space',
                       to_emails=to_emails,
                       subject=subject,
                       html_content=content)

        try:
            sendgrid_api_client = SendGridAPIClient(getattr(settings, 'SENDGRID_API_KEY', None))
            response = sendgrid_api_client.send(message)
            # TODO Remove console log for other kind of log
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            # TODO Remove console log for other kind of log
            print(e)
