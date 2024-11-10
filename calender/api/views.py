import random
from .serializers import (
    EventSerializer,
    TimeSerializer
)
from volunteer.models import Volunteer
from django.contrib.auth.models import (
    Group,
    User
)
from drf_spectacular.utils import extend_schema
from utils.response_model import Result
from calender.models import (
    Event,
    Time,
)
from rest_framework.views import APIView
from rest_framework import status
from calender.tasks import create_meeting


class EventApiView(APIView):

    @extend_schema(request=EventSerializer)
    def post(self, request, *args, **kwargs):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            try:
                volunteer = Volunteer.objects.get(email=serializer.data['email'])
                group = Group.objects.get(name="HR")
                interviewers = User.objects.filter(groups=group)
                time_obj = Time.objects.get(id=serializer.data["time_id"])
                if time_obj.number_reserve > 0:
                    event = Event.objects.get(time_id=time_obj.id)
                    if event.interviewee == volunteer:
                        return Result.error(status=status.HTTP_400_BAD_REQUEST,
                                            message="کاربر عزیز شما زمان مصاحبه خود را ست کرده اید.")
                    interviewer_new = interviewers.first()
                    # create meetings in google calender
                    event_obj = Event.objects.create(title=f"مصاحبه با{volunteer.first_name} ",
                                                     interviewer=interviewer_new,
                                                     interviewee=volunteer,
                                                     time=time_obj)
                    create_meeting.delay(start=time_obj.start_time, end=time_obj.end_time,
                                         date=time_obj.day,
                                         volunteer_email=volunteer.email,
                                         interviewer_email=interviewer_new.email,
                                         event_id=event_obj.id)
                    time_obj.number_reserve = time_obj.number_reserve + 1
                    time_obj.save()
                else:
                    event_obj = Event.objects.create(title=f"مصاحبه با {volunteer.first_name} ",
                                                     interviewer=interviewers[0],
                                                     interviewee=volunteer,
                                                     time=time_obj)
                    create_meeting.delay(start=time_obj.start_time, end=time_obj.end_time,
                                         date=time_obj.day,
                                         volunteer_email=volunteer.email,
                                         interviewer_email=interviewers[0].email,
                                         event_id=event_obj.id)
                    time_obj.number_reserve = time_obj.number_reserve + 1
                    time_obj.save()

                return Result.data({}, message="create successfully")
            except Volunteer.DoesNotExist:
                return Result.error(message="چنین کاربری وجود ندارد")

            except Event.DoesNotExist:
                return Result.error(message=" رویدادی وجود ندارد")

            except Exception as es:
                return Result.error(message=str(es))
        else:
            return Result.error(message=serializer.errors)

    @extend_schema()
    def get(self, request, *args, **kwargs):
        queryset = Time.objects.filter(number_reserve__lt=2)
        serializer = TimeSerializer(instance=queryset, many=True)
        return Result.data(data=serializer.data)
