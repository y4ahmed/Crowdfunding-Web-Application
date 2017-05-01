# Create your views here.
from frontend.forms import RegistrationForm
from .models import BaseUser
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from .forms import UploadFileForm
from Crypto.PublicKey import RSA


@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user_role = form.cleaned_data['user_role']

            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['pass1'],
                email=form.cleaned_data['email']
            )
            base = BaseUser.objects.create(
                user=user, user_role=user_role,
                RSAkey=RSA.generate(2048).exportKey()
            )

            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()

    variables = RequestContext(request, {
        'form': form
    })

    return render_to_response(
        'registration/register.html',
        variables,
    )


def register_success(request):
    return render_to_response(
        'registration/success.html',
    )


def upload_success(request):
    return render_to_response(
        'upload_success.html',
    )


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


def home(request):
    base = BaseUser.objects.get(user=request.user)
    return render_to_response(
        'home.html',
        {'user': base, 'type': base.user_role},
        context_instance=RequestContext(request)
    )


@csrf_protect
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/upload_success/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


def handle_uploaded_file(f):
    # Gets the file extension using substrings
    file_extension = f._get_name()[-3:]
    with open('lokahi_dropbox/temp.' + file_extension, 'wb+') as destination:
        for chunks in f.chunks():
            destination.write(chunks)
