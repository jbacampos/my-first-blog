from django.shortcuts import render
from django.template import RequestContext
from django.core.context_processors import csrf

def login_user(request):
    dic = {}
    dic.update(csrf(request))
    dic[‘state’] = state
    dic[‘username’] = username
    return render_to_response(‘auth.html’, dic)


# Create your views here.


# the last three lines should look so

