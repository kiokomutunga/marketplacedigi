from django.core.mail import send_mail
from django.conf import settings

def send_email_to_admin(subject, message, from_email=None):
    """
    Sends an email to the admin.
    """
    admin_email = [admin[1] for admin in settings.ADMINS]  # Extract admin emails from settings
    
    if not from_email:
        from_email = settings.DEFAULT_FROM_EMAIL
    
    send_mail(
        subject,
        message,
        from_email,
        admin_email,
        fail_silently=False,
    )
