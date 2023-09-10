from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
# Create your views here.
def members(request):
    MyMembers=Member.objects.all().values()
    template=loader.get_template('index.html')
    Context={
        'MyMembers':MyMembers
    }
    return HttpResponse(template.render(Context,request))
def details(request,id):
    MyMember=Member.objects.get(id=id)
    template=loader.get_template('detail.html')
    Context={
        'MyMember':MyMember
    }
    return HttpResponse(template.render(Context,request))