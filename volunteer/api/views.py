import datetime
from rest_framework import status
from rest_framework.views import APIView
from .serializers import (
    VolunteerCreateSerializer,
    VolunteerUpdateSerializer,
)
from volunteer.models import (
    Volunteer,
    Status,
    State,
    Task
)
from utils.response_model import Result
from drf_spectacular.utils import extend_schema
from volunteer.tasks import send_email_task


class VolunteerApiview(APIView):
    @extend_schema(request=VolunteerCreateSerializer)
    def post(self, request, *args, **kwargs):
        serializer = VolunteerCreateSerializer(data=request.data)
        if serializer.is_valid():
            state = State.objects.get(name="TEC")
            status_obj = Status.objects.get(state_id=state.id, key="Pending", order=1)
            serializer.validated_data["state"] = state
            serializer.validated_data["status"] = status_obj
            try:
                volunteer = Volunteer.objects.create(**serializer.validated_data)
                send_email_task.delay(name=serializer.validated_data["first_name"],
                                      receiver_email=serializer.validated_data["email"],
                                      volunteer_id = volunteer.id)
                return Result.data(data={}, status=status.HTTP_201_CREATED,
                                   message="created successfully")
            except Exception as ex:
                if 'UNIQUE constraint failed: volunteer_volunteer.email' in str(ex):
                    # Inform the user that the email is already taken
                    return Result.error(message=
                                        "داوطلب گرامی قبلا شما ثبت نام کرده اید")

        else:
            return Result.error(message=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(request=VolunteerUpdateSerializer)
    def put(self, request, *args, **kwargs):
        serializer = VolunteerUpdateSerializer(data=request.data)
        if serializer.is_valid():
            volunteer = Volunteer.objects.filter(email=serializer.validated_data["email"]).first()
            if volunteer.exists():
                Task.objects.filter(volunteer_id=volunteer.id).update(response_time=datetime.datetime.today(),
                                                                      file=serializer.validated_data["file"])
                return Result.data(data={}, status=status.HTTP_200_OK, message="update successfully")
            else:
                return Result.error(message="چنین داوطلبی وجود ندارد", status=status.HTTP_404_NOT_FOUND)
        else:
            return Result.error(message=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
