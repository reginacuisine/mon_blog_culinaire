from django.db import models

class Plat(models.Model):
    CATEGORIES = [
        ('TRAD', 'Traditionnel'),
        ('INTL', 'International'),
    ]
    nom = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='plats/') # Il faudra installer 'Pillow'
    categorie = models.CharField(max_length=4, choices=CATEGORIES)
    prix = models.DecimalField(max_digits=6, decimal_places=2)

    def __clt__(self):
        return self.nom