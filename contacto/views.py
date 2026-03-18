from django.shortcuts import render, redirect
from .forms import ContactoForm

def contacto_view(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            # Por ahora NO guardamos, solo simulamos envío
            return redirect("contacto_exito")
    else:
        form = ContactoForm()

    return render(request, "contacto/contacto.html", {"form": form})

def contacto_exito_view(request):
    return render(request, "contacto/exito.html")