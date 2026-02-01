from django.shortcuts import render, redirect # Ajoute redirect
from django.core.mail import send_mail
from django.contrib import messages # Pour les messages de succès
from .models import Plat

# ... (ta vue home reste la même)

def contact(request):
    if request.method == 'POST':
        # Ces noms doivent être IDENTIQUES à ceux de ton HTML
        nom = request.POST.get('nom')       # Correspond à name="nom"
        email = request.POST.get('email')   # Correspond à name="email"
        message = request.POST.get('message') # Correspond à n
        # Envoi du mail
        try:
            send_mail(
                f"Nouveau message de {nom} : {sujet}",
                message,
                'reginatonde44@gmail.com', # Ton mail expéditeur
                ['reginatonde44@gmail.com'], # Ton mail destinataire
                fail_silently=False,
            )
            messages.success(request, "Votre message a bien été envoyé ! Je vous répondrai bientôt.")
            return redirect('contact') # Recharge la page proprement
        except Exception as e:
            messages.error(request, "Une erreur est survenue lors de l'envoi. Réessayez plus tard.")
            
    return render(request, 'contact.html')