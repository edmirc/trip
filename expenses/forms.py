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
    class Meta:
        model = Citys
        fields = ['name', 'state']
        widgets = {
            'name': forms.Select(attrs={'class':'input-car'}),
            'state': forms.TextInput(attrs={'placeholder': 'Estado', 'class':'input-car'}),
        }
    
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['name'].queryset = Citys.objects.all()
        