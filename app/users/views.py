from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def register(request):
    if register.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm()
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, 'registration/register.html', context=context)