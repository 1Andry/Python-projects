from django.shortcuts import render
from .models import Skill, Test


def index(request):
    projects = Skill.objects.all()
    return render(request, 'skill/index.html', {'projects': projects})


def test(request):
    # test = Test.objects.all()
    return render(request, 'skill/test.html')