# urls.py
from django.urls import path

from chatDemo import consumers

urlpatterns = [
    # ...
    path('ws/test/', consumers.DatabaseChangesConsumer.as_asgi()),
]
