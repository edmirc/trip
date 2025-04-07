from django.db import models


class Car(models.Model):
    plate = models.CharField(max_length=7, unique=True, verbose_name='Paca')
    model = models.CharField(max_length=50, verbose_name='Modelo')
    km = models.IntegerField(verbose_name='Km')

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'
        ordering = ['plate']
    
    def save(self, *args, **kwargs):
        self.plate = self.plate.upper()
        self.model = self.model.title()
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.plate} - {self.model}'


class Citys(models.Model):
    name = models.CharField(max_length=50, verbose_name='Cidade')
    state = models.CharField(max_length=2, verbose_name='Estado')

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'
        ordering = ['name']
    
    def save(self, *args, **kwargs):
        self.name = self.name.title()
        self.state = self.state.upper()
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
class TypeExpense(models.Model):
    name = models.CharField(max_length=50, verbose_name='Tipo de despesa')

    class Meta:
        verbose_name = 'Tipo de despesa'
        verbose_name_plural = 'Tipos de despesas'
        ordering = ['name']
    
    def save(self, *args, **kwargs):
        self.name = self.name.title()
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class Tryp(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome da viagem')
    date_initial = models.DateField(verbose_name='Data inicial')
    date_final = models.DateField(verbose_name='Data final')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Carro')
    user = models.CharField(max_length=50, verbose_name='Usuário')
    km_total = models.IntegerField(verbose_name='Km total')
    atctive = models.BooleanField(default=True, verbose_name='Ativo')

    class Meta:
        verbose_name = 'Viagem'
        verbose_name_plural = 'Viagens'
        ordering = ['date_initial']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.name = self.name.title()
        self.user = self.user.title()
        return super().save(*args, **kwargs)

class Expense(models.Model):
    trip = models.ForeignKey(Tryp, on_delete=models.CASCADE, verbose_name='Viagem')
    date = models.DateField(verbose_name='Data')
    type = models.ForeignKey(TypeExpense, on_delete=models.CASCADE, verbose_name='Tipo de despesa')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Carro')
    qnt = models.FloatField(verbose_name='Quantidade')
    value = models.FloatField(verbose_name='Valor')
    city = models.ForeignKey(Citys, on_delete=models.CASCADE, verbose_name='Cidade')
    description = models.TextField(verbose_name='Descrição', blank=True, null=True)

    class Meta:
        verbose_name = 'Despesa'
        verbose_name_plural = 'Despesas'
        ordering = ['date']
    
    def __str__(self):
        return f'{self.trip} - {self.type}'


class Fuel(models.Model):
    expense = models.OneToOneField(Expense, on_delete=models.CASCADE, verbose_name='Despesa', related_name='fuel')
    km_initial = models.IntegerField(verbose_name='Km inicial')
    km_final = models.IntegerField(verbose_name='Km final')
    km_wheeled = models.IntegerField(verbose_name='Km rodado')
    averange = models.FloatField(verbose_name='Média')
    description = models.TextField(verbose_name='Descrição', blank=True, null=True)

    class Meta:
        verbose_name = 'Combustível'
        verbose_name_plural = 'Combustíveis'
        ordering = ['expense']

    def __str__(self):
        return str(self.km_final)