from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import motorstate, controlstate


def json(request):

    controldata = [controlstate.objects.latest(), ]
    motordata = [motorstate.objects.latest(), ]
    data = {}
    data['motor'] = motordata
    data['control'] = controldata
    jsondata = serializers.serialize("json", data)
    return HttpResponse(jsondata)
# Create your views hereo
