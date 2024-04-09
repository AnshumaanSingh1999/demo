from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import users


# def (request):
#   template = loader.get_template('myfirst.html')
#   return HttpResponse(template.render())

def home(request):
  return HttpResponse("Hello World")
def badaKaam(request):
  template=loader.get_template('child.html')
  return HttpResponse(template.render())
def usersview(request):
  usersdata=users.objects.all()
  return render(request,"users.html",{"users":usersdata})
