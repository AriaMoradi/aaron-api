from django.urls import path

from .views import DateTimeView

urlpatterns = [
    path('datetime', DateTimeView.as_view())
]