from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse

def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({
            'result': True
        })
    else:
        return JsonResponse({
            'result': False
        })

def logout_user(request):
    logout(request)
    return JsonResponse({
        'result': True
    })
