from rest_framework import status
from rest_framework import viewsets
from .serializers import VolunteerSerializer
from volunteer.models import Volunteer, Status, State
from utils.response_model import Result
from drf_spectacular.utils import extend_schema


class VolunteerCreate(viewsets.ViewSet):
    queryset = Volunteer.objects.all()

    @extend_schema(request=VolunteerSerializer)
    def create(self, request, *args, **kwargs):
        serializer = VolunteerSerializer(data=request.data)
        if serializer.is_valid():
            state = State.objects.get_or_create(name="TEC")
            status_obj = Status.objects.get_or_create(name="Pending")
            serializer.validated_data["state"] = state[0]
            serializer.validated_data["status"] = status_obj[0]
            Volunteer.objects.create(**serializer.validated_data)
            return Result.data(data=serializer.data, status=status.HTTP_201_CREATED,
                               message="created successfully")
        else:
            return Result.error(message=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
