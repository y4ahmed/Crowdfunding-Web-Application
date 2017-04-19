from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, render
from messaging.forms import *
from django.contrib.auth.models import User
from frontend.models import *


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

            if form.cleaned_data['encrypt']:
                # encrypt
                receiver_user = User.objects.get(username=r)
                receiver_base_user = BaseUser.objects.get(user=receiver_user)
                receiver_RSAkey = receiver_base_user.RSAkey
                m = str(receiver_RSAkey.encrypt(m.encode('utf-8'), "not needed".encode('utf-8'))[0])
                message = Message.objects.create(subject=p,message=m, receiver=r, sender=s)
                return render(request, 'messaging/send_message.html', {'form': MessageForm()})
            else:
                # leave as the same
                message = Message.objects.create(subject=p,message=m, receiver=r, sender=s)
                return render(request, 'messaging/send_message.html', {'form': MessageForm()})
    else:
        form = MessageForm()
        return render(request,'messaging/send_message.html', {'form': form})

@csrf_protect
def receive_message(request):
    messages = Message.objects.filter(receiver=request.user.username)
    if len(messages) != 0:
        return render(request, 'messaging/receive_message.html',{'messages': messages})
    else:
        return render(request, 'messaging/receive_message.html',)


def delete_message(request):
    if request.method == 'POST':
        form = DeleteForm(data=request.POST)
        if form.is_valid():
            index = form.cleaned_data['message']
            m = Message.objects.get(id=index)
            m.delete()
            messages = Message.objects.filter(receiver=request.user.username)
            return render(request, 'messaging/receive_message.html',{'messages': messages})

def decrypt_message(request):
    return render(request, 'messaging/receive_message.html',)
