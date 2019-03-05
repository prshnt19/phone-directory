from django.shortcuts import render
from .models import PhoneDirectory
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.


def phonedir(request):
    subscibers = (PhoneDirectory.objects.all())
    return render(request, 'index.html', {'subscribers': subscibers})


def add(request):
    return render(request, 'add.html')


def addsubscriber(request):
    name = request.POST.get('name')
    number = request.POST.get('number')
    subscriber = PhoneDirectory(Name=name, Number=number)
    subscriber.save()
    return HttpResponseRedirect('/')


def delete(request, id):
    PhoneDirectory.objects.get(id=id).delete()
    return HttpResponseRedirect('/')
