import time
import threading

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Student, SignalLog


@receiver(post_save, sender=Student)
def student_signal(sender, instance, created, **kwargs):

    print("\nSignal Started")

    # Question 2 Proof
    print("Signal Thread ID:", threading.get_ident())

    # Question 1 Proof
    time.sleep(5)

    # Question 3 Proof
    SignalLog.objects.create(message="Signal Executed")

    print("Signal Completed\n")