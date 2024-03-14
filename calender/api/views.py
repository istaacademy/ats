import random
from .serializers import (
    EventSerializer,
    TimeSerializer
)
from volunteer.models import Volunteer, Status
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
from services.google.set_calender import set_meeting


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
                        return Result.error(message="کاربر عزیز شما قبلا زمان مضاحبه خود را ست کرده اید.")
                    user_interviewer = event.interviewer
                    interviewers_new = [interviewer_new for interviewer_new in interviewers if
                                        user_interviewer != interviewer_new]
                    print(interviewers_new)
                    interviewer_new = random.choices(interviewers_new)[0]
                    # create meetings in google calender
                    link_meeting = set_meeting(start=time_obj.start_time, end=time_obj.end_time,
                                               date=time_obj.day,
                                               volunteer_email=volunteer.email,
                                               interviewer_email=interviewer_new.email)

                    Event.objects.create(title=f"مصاحبه با{volunteer.first_name} ",
                                         interviewer=interviewer_new,
                                         interviewee=volunteer,
                                         time=time_obj,
                                         link_meeting=link_meeting)
                    time_obj.number_reserve = time_obj.number_reserve + 1
                    time_obj.save()
                else:
                    link_meeting = set_meeting(start=time_obj.start_time, end=time_obj.end_time,
                                               date=time_obj.day,
                                               volunteer_email=volunteer.email,
                                               interviewer_email=interviewers[0].email)
                    Event.objects.create(title=f"مصاحبه با {volunteer.first_name} ",
                                         interviewer=interviewers[0],
                                         interviewee=volunteer,
                                         time=time_obj,
                                         link_meeting=link_meeting)
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
