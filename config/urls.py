from django.contrib import admin
from django.urls import path
from cuisine import views
from django.conf import settings # Pour accéder à tes réglages MEDIA
from django.conf.urls.static import static # Pour servir les fichiers statiques

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact_page'),
    
]

# Cette ligne est CRUCIALE pour afficher tes photos de plats pendant le développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)