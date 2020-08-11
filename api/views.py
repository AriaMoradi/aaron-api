from rest_framework import mixins, generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import DateTime
from .serializers import DateTimeSerializer


class DateTimeView(mixins.CreateModelMixin,
                   generics.GenericAPIView):
    queryset = DateTime.objects.all()
    serializer_class = DateTimeSerializer

    def last(self, request, *args, **kwargs):
        instance = self.queryset.last()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get(self, request, *args, **kwargs):
        return self.last(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
