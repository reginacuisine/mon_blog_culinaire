from django.shortcuts import render
from .models import Plat  # On importe ton modèle Plat pour voir ce qu'il y a en stock

# Dans views.py
def home(request):
    cat_slug = request.GET.get('categorie')
    if cat_slug:
        plats = Plat.objects.filter(categorie=cat_slug)
    else:
        plats = Plat.objects.all()
    return render(request, 'accueil.html', {'plats': plats})

def contact(request):
    # Cette vue affiche uniquement la page de contact
    return render(request, 'contact.html')