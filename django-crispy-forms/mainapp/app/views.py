from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import PersonForm


def home_view(request):
    if request.method == 'POST':
        form  = PersonForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account created for {email}!')
            form.save()
            return redirect('home')

        else:
            messages.warning(request, f'Account already Exist!')

    else:
        form = PersonForm()

    return render(request, 'home.html', {'form': form})
