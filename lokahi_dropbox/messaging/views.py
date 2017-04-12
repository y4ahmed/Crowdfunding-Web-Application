from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, render
from messaging.forms import *
from django.contrib.auth.models import User


# Create your views here.
@csrf_protect
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            m = form.cleaned_data['message']
            r = form.cleaned_data['receiver']
            form.validate()
            s = request.user.username
            p = form.cleaned_data['subject']
            message = Message.objects.create(subject=p,message=m, receiver=r, sender=s)
            return render(request, 'messaging/send_message.html', {'form': form})
    else:
        form = MessageForm()
        return render(request,'messaging/send_message.html', {'form': form})

@csrf_protect
def receive_message(request):
    messages = Message.objects.filter(receiver=request.user.username)
    if len(messages) != 0:
        return render_to_response('messaging/receive_message.html',{'messages': messages})
    else:
        return render_to_response('messaging/receive_message.html',)
