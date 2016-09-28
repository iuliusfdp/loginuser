# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*-
from django.shortcuts import render,HttpResponseRedirect,render_to_response, redirect,HttpResponse
from django.template.context import RequestContext
from django.contrib.auth import  login,authenticate,logout
from models import User


 
def login(request):
    if request.user.is_authenticated():
        return render_to_response('VistaLogin.html', context_instance=RequestContext(request))
    return render_to_response('VistaLogin.html', context_instance=RequestContext(request))

def loginUser(request):
    if request.method=="POST":
        try:
            username = request.POST['name']
            password = request.POST['password']
            authent = User.objects.filter(username=username, password=password)
            print authent
            if not authent:
                return render_to_response('VistaLoginError.html', context_instance=RequestContext(request))
            else:
                return render_to_response('VistaLoginExitoso.html', context_instance=RequestContext(request))
        except Exception as e:
            print e