from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, render



# Create your views here.
@csrf_protect
def send_message(request):
    return render_to_response(
    'messaging/send_message.html',
    )
