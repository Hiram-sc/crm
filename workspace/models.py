from django.db import models

class Contact(models.Model):
    STATUS_CHOICES = [
        ('novo', 'Novo'),
        ('pendente', 'Pendente'),
        ('lido', 'Lido'),
        ('respondido', 'Respondido'),
        ('fechado', 'Fechado')
    ]

    name = models.CharField(max_length=150, blank=False, null=False)
    email = models.EmailField(max_length=150, blank=False, null=False, unique=True)
    phone = models.CharField(max_length=20, blank=False, null=False)
    occupation = models.CharField(max_length=60, blank=False, null=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Novo')
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    last_interaction_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'contacts'
        ordering = ['-created_at']

    def __str__(self):
        return f' Contato: {self.name} - {self.occupation}' 

