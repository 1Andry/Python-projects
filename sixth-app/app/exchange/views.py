from django.shortcuts import render
import requests


def exchange(request):
    response = request.get(url ='https://cdn.cur.su/api/latest.json').json()
    currencies = response.get('rates')
    if request.method == 'GET':
        context = {
            'currencies': currencies
        }

        return render(request, template_name='exchange/index.html', context=context)
