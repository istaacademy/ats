import json
from rest_framework import serializers
from volunteer.models import Volunteer


class VolunteerSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=300)
    email = serializers.RegexField(regex=r'^[a-zA-Z0-9._%+-]+@gmail\.com$')
    phone_number = serializers.RegexField(regex=r'09(1[0-9]|3[1-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}', max_length=11)
    year_of_birth = serializers.IntegerField()
    url_linkedin = serializers.URLField()

    class Meta:
        model = Volunteer
        fields = ("first_name", "last_name", "email", "phone_number", "year_of_birth", "url_linkedin")

