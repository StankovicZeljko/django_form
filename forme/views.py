# form/views.py
from django.shortcuts import render, redirect
from .forms import PotentialUserInformationForm

def form_view(request):
    if request.method == 'POST':
        form = PotentialUserInformationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PotentialUserInformationForm()
    return render(request, 'form/form.html', {'form': form})

def success_view(request):
    return render(request, 'form/success.html')
