from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def adspace_worpress_pugin(request):
    template = loader.get_template('main/index.html')
    return HttpResponse(template.render({}, request))
