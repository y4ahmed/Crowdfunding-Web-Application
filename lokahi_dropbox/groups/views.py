from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, render

# Create your views here.
@csrf_protect
def groups(request):
    return render(request, 'group/groups.html',)

def create_group(request):
    if request.method == 'POST':
        
        return render(request, 'group/view_group.html',)
    else:
        return render(request, 'group/create_group.html',)

def view_group(request):
    return render(request, 'group/view_group.html',)
