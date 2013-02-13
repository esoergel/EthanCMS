from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.contrib.auth import login, logout, authenticate
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import RequestContext

def login_user(request):
    ctxt = RequestContext(request)
    if request.method == "POST":
        user = authenticate(
            username = request.POST['username'],
            password = request.POST['password'],
            )
        if user and user.is_staff:
            login(request, user)
            return redirect('/')
        ctxt['error'] = True
    return render_to_response('login.html', ctxt)


def logout_user(request):
    logout(request)
    return redirect('/')