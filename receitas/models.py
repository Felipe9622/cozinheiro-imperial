from django.db import models
# Used to generate URLs by reversing the URL patterns
from django.urls import reverse


class Receita(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=500)

    def __str__(self):
        """String for representing the Model object."""
        return self.titulo


    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('detail', args=[str(self.id)])