from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages

def contact(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        email_client = request.POST.get('email')
        message_client = request.POST.get('message')

        try:
            send_mail(
                f"Contact de {nom}",
                f"De: {nom} ({email_client})\n\n{message_client}",
                'reginatonde44@gmail.com',
                ['reginatonde44@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, "Message envoyé !")
            return redirect('contact_page')
        except Exception:
            messages.error(request, "Erreur d'envoi.")
            
    return render(request, 'contact.html')
def home(request):
    return render(request, 'accueil.html') # On change home.html par accueil.html