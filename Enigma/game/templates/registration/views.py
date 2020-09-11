from django.shortcuts import redirect, render

from .forms import RegisterForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    form = RegisterForm()
    return render(request, 'registration/registrate.html', {'form': form})