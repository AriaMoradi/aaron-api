from rest_framework.generics import ListCreateAPIView

from .models import DateTime
from .serializers import DateTimeSerializer


class DateTimeView(ListCreateAPIView):
    queryset = DateTime.objects.all()
    serializer_class = DateTimeSerializer

