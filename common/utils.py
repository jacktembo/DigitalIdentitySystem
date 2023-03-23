from django.conf import settings
from django.core.mail import EmailMessage
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User


class SendEmailAPIView(APIView):
    """
    Send email to user. Pass email, subject and message in the request body.
    Then call the post method to send the email.
    """

    def post(self, request):
        """
        Send email using the Message class
        :param request:
        :return:
        """
        email = request.data.get('email')
        subject = request.data.get('subject')
        message = request.data.get('message')
        try:
            email = EmailMessage(
                subject, message, to=[email], from_email=settings.EMAIL_HOST_USER
            )
            email.send()
            return Response({'message': 'Email sent successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': 'Email not sent'}, status=status.HTTP_400_BAD_REQUEST)


