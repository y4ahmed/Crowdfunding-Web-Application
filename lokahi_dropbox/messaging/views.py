from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from messaging.forms import Message
from django.contrib.auth.models import User
from frontend.models import BaseUser
from messaging.forms import MessageForm, DeleteForm, DecryptMessageForm
from Crypto.PublicKey import RSA


@csrf_protect
def messaging(request):
    base = BaseUser.objects.get(user=request.user)
    return render(
        request,
        'messaging/messaging.html',
        {'type': base.user_role}
    )


@csrf_protect
def send_message(request):
    base = BaseUser.objects.get(user=request.user)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            m = form.cleaned_data['message']
            r = (form.cleaned_data['receiver']).strip()
            form.validate()
            s = request.user.username
            p = form.cleaned_data['subject']

            if r == s:
                return render(
                    request,
                    'messaging/send_message.html',
                    {'form': MessageForm(), 'type': base.user_role,
                     'is_yourself': True}
                )
                # raise Error("cannot send a message to yourself")

            if form.cleaned_data['encrypt']:
                # encrypt
                receiver_user = User.objects.get(username=r)
                receiver_base_user = BaseUser.objects.get(user=receiver_user)
                receiver_RSAkey = RSA.importKey(receiver_base_user.RSAkey)
                m = str(receiver_RSAkey.encrypt(
                    m.encode('utf-8'), "not needed".encode('utf-8'))[0])
                message = Message.objects.create(
                    subject=p, message=m, receiver=r, sender=s, encrypt=True)
                return render(
                    request,
                    'messaging/send_message.html',
                    {'form': MessageForm(), 'type': base.user_role,
                     'is_yourself': False}
                )
            else:
                # leave as the same
                message = Message.objects.create(
                    subject=p, message=m, receiver=r, sender=s, encrypt=False)
                return render(
                    request,
                    'messaging/send_message.html',
                    {'form': MessageForm(), 'type': base.user_role,
                     'is_yourself': False}
                )
    else:
        form = MessageForm()
        return render(
            request,
            'messaging/send_message.html',
            {'form': form, 'type': base.user_role, 'is_yourself': False}
        )


@csrf_protect
def receive_message(request):
    base = BaseUser.objects.get(user=request.user)
    messages = Message.objects.filter(receiver=request.user.username)
    if len(messages) != 0:
        return render(
            request,
            'messaging/receive_message.html',
            {'messages': messages, 'type': base.user_role}
        )
    else:
        return render(request, 'messaging/receive_message.html',)


def delete_message(request):
    base = BaseUser.objects.get(user=request.user)
    if request.method == 'POST':
        form = DeleteForm(data=request.POST)
        if form.is_valid():
            index = form.cleaned_data['message']
            print(index)
            m = Message.objects.get(id=index)
            m.delete()
            messages = Message.objects.filter(receiver=request.user.username)
            return render(
                request,
                'messaging/receive_message.html',
                {'messages': messages, 'type': base.user_role}
            )


def decrypt_message(request):
    base = BaseUser.objects.get(user=request.user)
    if request.method == 'POST':
        form = DecryptMessageForm(data=request.POST)
        if form.is_valid():
            message = Message.objects.get(id=form.cleaned_data['message'])
            if message.encrypt:
                # attempt decrypting only if it was encrypted to begin with
                # user your private key for decryption
                # set the message encrypt field to false now so that we don't
                # try to decrypt it again replace the message body and the
                # encrypt fields
                user = User.objects.get(username=request.user.username)
                base_user = BaseUser.objects.get(user=user)
                # print(base_user.RSAkey)
                receiver_RSAkey = RSA.importKey(base_user.RSAkey)
                byte_cipher = eval(message.message)
                plain = receiver_RSAkey.decrypt(byte_cipher)
                message.encrypt = False
                message.message = plain.decode('utf-8')
                message.save()
            else:
                # throw error
                messages = Message.objects.filter(
                    receiver=request.user.username).order_by('id')
                return render(
                    request,
                    'messaging/receive_message.html',
                    {'messages': messages, 'type': base.user_role,
                     'is_decrypted': True}
                )

            messages = Message.objects.filter(
                receiver=request.user.username).order_by('id')

    return render(
        request,
        'messaging/receive_message.html',
        {'messages': messages, 'type': base.user_role, 'is_decrypted': False}
    )
