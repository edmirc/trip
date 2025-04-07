from django.contrib import admin
from expenses.models import Car, Citys, TypeExpense, Tryp, Expense


@admin.register(Citys)
class CitysAdmin(admin.ModelAdmin):
    list_display = ('name', 'state')
    search_fields = ('name', 'state')
    list_filter = ('state',)
    model = Citys
    ordering = ('name',)