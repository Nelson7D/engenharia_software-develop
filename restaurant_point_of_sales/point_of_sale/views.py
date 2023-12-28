from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.conf import settings



# Create your views here.

@login_required
def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    context = {"latest_question_list": 'latest_question_list'}
    return render(request, "point_of_sale/index.html", context)

