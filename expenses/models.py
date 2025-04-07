from django.db import models

class Car(models.Model):
    plate = models.CharField(max_length=7, unique=True, verbose_name='Paca')
    model = models.CharField(max_length=50, verbose_name='Modelo')
    km = models.IntegerField(verbose_name='Km')

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'
        ordering = ['plate']
    
    def __str__(self):
        return f'{self.plate} - {self.model}'
    
class Citys(models.Model):
    name = models.CharField(max_length=50, verbose_name='Cidade')
    state = models.CharField(max_length=2, verbose_name='Estado')

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'
        ordering = ['name']
    
    def __str__(self):
        return f'{self.name}'

