from django.urls import path

from comments.consumers import CommentConsumer


websocket_urlpatterns = [
    path('comment/', CommentConsumer),
]
