from django.shortcuts import render, get_object_or_404
from .models import Bl


def bl(request):
    blogs = Bl.objects.order_by('date')
    return render(request, 'bl/bl.html', {'blogs': blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Bl, pk=blog_id)
    return render(request, 'bl/detail.html', {'blog': blog})
