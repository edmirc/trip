from django.contrib import admin
from expenses.models import Car, Citys, TypeExpense, Tryp, Expense


@admin.register(Citys)
class CitysAdmin(admin.ModelAdmin):
    list_display = ('name', 'state')
    search_fields = ('name', 'state')
    list_filter = ('state',)
    model = Citys
    ordering = ('name',)

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('plate', 'model', 'km')
    search_fields = ('plate', 'model')
    list_filter = ('model',)
    model = Car
    ordering = ('plate',)

@admin.register(TypeExpense)
class TypeExpenseAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    model = TypeExpense
    ordering = ('name',)