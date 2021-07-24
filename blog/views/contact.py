
from django.shortcuts import redirect, render
from blog.forms import ContactForm
from blog.models import ContactModel


def contact(request):
    form = ContactForm(initial={
        'fullname': 'Elmar'
    })
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact.save()
            return redirect('homepage')
    context = {
        'form': form,
    }
    return render(request, 'pages/contact.html', context=context)
