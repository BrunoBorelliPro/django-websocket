from django.urls import path
from core.views import ChatConsumer

from core import views

urlpatterns = [
    path("", views.index, name="index"),
]


from django.urls import path
