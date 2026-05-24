import time
import threading

from django.db import transaction
from django.http import HttpResponse

from .models import Student


# QUESTION 1
def question1(request):

    start = time.time()

    Student.objects.create(name="Question1")

    end = time.time()

    total = end - start

    return HttpResponse(
        f"Question 1 Completed in {total} seconds"
    )


# QUESTION 2
def question2(request):

    print("Caller Thread ID:", threading.get_ident())

    Student.objects.create(name="Question2")

    return HttpResponse(
        "Check terminal for thread IDs"
    )


# QUESTION 3
def question3(request):

    try:

        with transaction.atomic():

            Student.objects.create(name="Question3")

            raise Exception("Rollback Transaction")

    except Exception as e:

        return HttpResponse(
            f"Transaction Rolled Back: {e}"
        )