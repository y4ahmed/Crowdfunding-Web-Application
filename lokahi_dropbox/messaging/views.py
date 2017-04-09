from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, render
from messaging.forms import *
from django.contrib.auth.models import User


# Create your views here.
@csrf_protect
def send_message(request):
    if request.method == 'GET':
        form = MessageForm(request.GET)
        if form.is_valid():
            m = form.cleaned_data['message']
            r = form.cleaned_data['receiver']
            form.validate()
            message = Message.objects.create(message=m, receiver=r)
            return render_to_response('messaging/send_message.html',)
        else:
            return render_to_response('messaging/send_message.html',)
