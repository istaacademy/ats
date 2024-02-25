import random
from rest_framework import viewsets
from .serializers import EventSerializer, TimeSerializer
from volunteer.models import Volunteer
from django.contrib.auth.models import Group, User
from drf_spectacular.utils import extend_schema
from utils.response_model import Result
from calender.models import Event, Time


class EventViewSet(viewsets.ViewSet):
    queryset = Time.objects.all()

    @extend_schema()
    def create(self, request, *args, **kwargs):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            try:
                volunteer = Volunteer.objects.get(email=serializer.data['email'])
                group = Group.objects.get(name="HR")
                interviewers = User.objects.filter(groups=group)
                time_obj = Time.objects.get(id=serializer.data["time_id"])
                if time_obj.number_reserve > 0:
                    obj = Event.objects.get(time_id=time_obj.id).interviewer
                    interviewees = [interviewer_new for interviewer_new in interviewers if
                                    obj != interviewer_new]
                    Event.objects.create(title=f"{volunteer.first_name} is interviewed",
                                         interviewer=random.choices(interviewees)[0],
                                         interviewee=volunteer,
                                         time=time_obj)
                    time_obj.number_reserve = time_obj.number_reserve + 1
                    time_obj.save()
                else:
                    Event.objects.create(title=f"{volunteer.first_name} is interviewed",
                                         interviewer=interviewers[0],
                                         interviewee=volunteer,
                                         time=time_obj)
                    time_obj.number_reserve = time_obj.number_reserve + 1
                    time_obj.save()

                return Result.data({})
            except Volunteer.DoesNotExist:
                return Result.error(message="چنین کاربری وجود ندارد")
        else:
            return Result.error(message=serializer.errors)

    @extend_schema(responses=TimeSerializer)
    def list(self, request, *args, **kwargs):
        serializer = TimeSerializer(instance=self.queryset.filter(number_reserve__lt=2), many=True)
        return Result.data(data=serializer.data)
