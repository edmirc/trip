from expenses.models import Car, Citys, TypeExpense, Tryp, Expense
from django import forms 


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['plate', 'model', 'km']
        widgets = {
            'plate': forms.TextInput(attrs={'placeholder': 'Placa', 'class':'input-car'}),
            'model': forms.TextInput(attrs={'placeholder': 'Modelo', 'class':'input-car'}),
            'km': forms.NumberInput(attrs={'placeholder': 'Km', 'class':'input-car'}),
        }

class CityForm(forms.ModelForm):
    name = forms.ChoiceField(
        choices=[(city.id, city.name) for city in Citys.objects.all()],
        widget=forms.Select(attrs={'class': 'select-form'}),
        label='Cidade')
    class Meta:
        model = Citys
        fields = ['name', 'state']
        widgets = {
            'state': forms.TextInput(attrs={'placeholder': 'Estado', 'class':'input-form'}),
        }
     

class TypeExpenseForm(forms.ModelForm):
    class Meta:
        model = TypeExpense
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Tipo de despesa', 'class':'input-form'}),
        }


class TrypForm(forms.ModelForm):
    car = forms.ChoiceField(
        choices=[(car.id, car.plate) for car in Car.objects.all()],
        widget=forms.Select(attrs={'class': 'select-form'}),
        label='Carro')
    class Meta:
        model = Tryp
        fields = ['name', 'date_initial', 'date_final', 'car']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nome da viagem', 'class':'input-form'}),
            'date_initial': forms.DateInput(attrs={'placeholder': 'Data inicial', 'class':'input-form'}),
            'date_final': forms.DateInput(attrs={'placeholder': 'Data final', 'class':'input-form'}),
        }