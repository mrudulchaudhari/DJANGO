from django.db import models
from django.utils import timezone

class ChaiVariety(models.Model):  # Capital C and V
    CHAI_TYPE_CHOICE = [
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('PL', 'PLAIN'),
        ('KL', 'KIWI'),
        ('EL', 'ELAICHI'),
    ]
    
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="chais/")
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE, default='PL')
    description = models.TextField(default='')

    def __str__(self):
        return self.name