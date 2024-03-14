from django.db.models.signals import post_save
from django.dispatch import receiver
from volunteer.models import (
    Volunteer,
    State,
    Status,
)


@receiver(post_save, sender=Volunteer)
def update_volunteer(sender, created, instance, **kwargs):
    # Avoid recursion if this function triggers another save
    if kwargs.get('update_fields') is not None:
        return

    if not created and instance.status.key == "Accept":
        state_obj = State.objects.filter(name__in=["HR", "PAYMENT"])
        try:
            if instance.state.name == "TEC":
                instance.state = state_obj.get(name="HR")
                instance.status = Status.objects.get(order=1, state=state_obj.get(name="HR"))
            else:
                instance.state = state_obj.get(name="PAYMENT")
                instance.status = Status.objects.get(order=1, state=state_obj.get(name="PAYMENT"))

            instance.save(update_fields=['state', 'status'])
        except (KeyError, State.DoesNotExist, Status.DoesNotExist) as e:
            # Handle the error or log it
            print(f"An error occurred: {e}")