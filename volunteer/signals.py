from django.db.models.signals import post_save
from django.dispatch import receiver
from volunteer.models import (
    Volunteer,
    State,
    Status,
)
from volunteer.tasks import (
    send_email_accept_task,
    send_email_reject_task,
    send_email_accept_hr,
)


@receiver(post_save, sender=Volunteer)
def update_volunteer(sender, created, instance, **kwargs):
    # Avoid recursion if this function triggers another save
    if kwargs.get('update_fields') is not None:
        return

    if not created and instance.status.key == "Accept":
        state_obj = State.objects.filter(name__in=["HR", "PAYMENT"])
        try:
            if instance.state.name == "TEC" and not instance.is_special:
                instance.state = state_obj.get(name="HR")
                instance.status = Status.objects.get(order=1, state=state_obj.get(name="HR"))
                send_email_accept_task.delay(instance.first_name, instance.email)
            elif instance.state.name == "TEC":
                instance.state = state_obj.get(name="PAYMENT")
                instance.status = Status.objects.get(order=1, state=state_obj.get(name="PAYMENT"))
                send_email_accept_hr.delay(instance.first_name, instance.email)
            instance.save(update_fields=['state', 'status'])
        except (KeyError, State.DoesNotExist, Status.DoesNotExist) as e:
            # Handle the error or log it
            print(f"An error occurred: {e}")
    elif not created and instance.status.key == "Reject":
        send_email_reject_task.delay(instance.first_name, instance.email)
