from rest_framework import serializers

from .models import DateTime


class DateTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DateTime
        fields = ('date_year', 'date_month', 'date_day', 'time_hour',
                'time_minute',
                'time_second'
        )
