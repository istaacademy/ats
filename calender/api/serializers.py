from rest_framework import serializers

from calender.models import Event, Time


class EventSerializer(serializers.ModelSerializer):
    time_id = serializers.IntegerField()
    email = serializers.RegexField(regex=r'^[a-zA-Z0-9._%+-]+@gmail\.com$')

    class Meta:
        model = Event
        fields = ('time_id', 'email')


class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = ('id', 'day', "start_time", "end_time")
