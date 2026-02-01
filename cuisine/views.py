from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Plat

def contact(request):
    if request.method == 'POST':
        # On récupère les données avec les noms exacts de ton HTML
        nom = request.POST.get('nom')
        email_client = request.POST.get('email')
        message_client = request.POST.get('message')

        try:
            # Envoi du mail
            send_mail(
                f"Nouveau message de {nom}", # Sujet simplifié (plus besoin de la variable sujet)
                f"De: {nom} ({email_client})\n\nMessage:\n{message_client}", # Contenu du mail
                'reginatonde44@gmail.com', 
                ['reginatonde44@gmail.com'], 
                fail_silently=False,
            )
            messages.success(request, "Votre message a bien été envoyé ! Je vous répondrai bientôt.")
            return redirect('contact_page') # Utilise le nom exact défini dans tes urls.py
        except Exception as e:
            messages.error(request, "Une erreur est survenue lors de l'envoi. Réessayez plus tard.")
            
    return render(request, 'contact.html')
