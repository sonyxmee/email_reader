from django.shortcuts import render
from .models import EmailMessage


def message_list(request):
    messages = EmailMessage.objects.all()
    return render(request, 'email_messages/message_list.html', {'messages': messages})

