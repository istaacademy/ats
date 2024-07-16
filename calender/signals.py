from django.db.models.signals import post_save
from django.dispatch import receiver
from calender.models import Event
from volunteer.models import (
    Volunteer,
    State,
    Status,
)
from volunteer.tasks import send_email_accept_hr


@receiver(post_save, sender=Event)
def update_volunteer(sender, created, instance, **kwargs):
    # Avoid recursion if this function triggers another save
    if kwargs.get('update_fields') is not None:
        return
    if not created and instance.status == "Accept":
        state_obj = State.objects.get(name="PAYMENT")
        try:
            volunteer_obj = Volunteer.objects.get(id=instance.interviewee_id)
            volunteer_obj.state = state_obj
            volunteer_obj.status = Status.objects.get(order=1, state=state_obj)
            volunteer_obj.save(update_fields=['state', 'status'])
            send_email_accept_hr(volunteer_obj.first_name, volunteer_obj.email)
        except (KeyError, State.DoesNotExist, Status.DoesNotExist) as e:
            # Handle the error or log it
            print(f"An error occurred: {e}")
