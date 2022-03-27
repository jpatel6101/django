from django.shortcuts import render

from .forms import PersonForm
from .models import Person


def home_view(request):

    form = PersonForm()

    context = {"form": form}
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            fage = form.cleaned_data['fage']

            p = Person(first_name=firstname, last_name=lastname, age=fage)
            p.save()
            return render(request, "home.html", context)

        else:
            context = {"form": form}
    return render(request, "home.html", context)

