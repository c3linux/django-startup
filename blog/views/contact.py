
from django.shortcuts import render
from django.http import HttpResponse


def contact(request):
    context = {
        'name': 'Elmar'
    }
    return render(request, 'pages/contact.html', context=context)
