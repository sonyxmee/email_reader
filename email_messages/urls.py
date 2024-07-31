from django.urls import path, re_path

from email_messages import consumers
# from .views import message_list


# urlpatterns = [
#     path('', message_list, name='message_list'),
#     path('', message_list, name='message_list'),
# ]
websocket_urlpatterns = [
    re_path(r'ws/email_messages/', consumers.EmailConsumer.as_asgi()),
]