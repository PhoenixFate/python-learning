from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def set_session(request):
    request.session['username'] = "tom"
    request.session['password'] = '123456'
    return HttpResponse("设置session成功")


def get_session(request):
    username = request.session.get("username")
    password = request.session.get("password")
    return HttpResponse(username + " : " + password)
