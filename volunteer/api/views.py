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
)
from utils.response_model import Result
from drf_spectacular.utils import extend_schema
from services.google.send_gmail import send_email


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
                print(serializer.validated_data)
                obj = Volunteer.objects.create(**serializer.validated_data)

                is_send = send_email(serializer.validated_data["first_name"],
                                     serializer.validated_data["last_name"],
                                     serializer.validated_data["email"], )
                obj.is_send_email = is_send
                obj.save()
                return Result.data(data={}, status=status.HTTP_201_CREATED,
                                   message="created successfully")
            except Exception as ex:
                if 'UNIQUE constraint failed: volunteer_volunteer.email' in str(ex):
                    # Inform the user that the email is already taken
                    return Result.error(message=
                                        "Error: This email address is already in use. Please choose a different email.")

        else:
            return Result.error(message=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(request=VolunteerUpdateSerializer)
    def put(self, request, *args, **kwargs):
        serializer = VolunteerUpdateSerializer(data=request.data)
        if serializer.is_valid():
            volunteer = Volunteer.objects.filter(email=serializer.validated_data["email"])
            if volunteer.exists():
                volunteer.update(url_github=serializer.validated_data["url_github"])
                volunteer.first().save()
                return Result.data(data={}, status=status.HTTP_200_OK, message="update successfully")
            else:
                return Result.error(message="چنین داوطلبی وجود ندارد", status=status.HTTP_404_NOT_FOUND)
        else:
            return Result.error(message=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
