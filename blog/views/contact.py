
from django.shortcuts import render
from django.http import HttpResponse


def contact(request):
    context = {
        'name': 'Elmar',
        'number': 10,
        'key': 'hey hello alright'
    }
    return render(request, 'pages/contact.html', context=context)
