from django.contrib import admin
from models import *

def approve_withdrawals(modeladmin, request, queryset):
	for obj in queryset.filter(approved=False):
		obj.approve()
approve_withdrawals.short_description = 'Approve selected withdrawals'

class UnitPackAdmin(admin.ModelAdmin):
	list_display = ('timestamp', 'user', 'quantity', 'expires',
		'initial_quantity', 'is_valid')
	exclude = ('initial_quantity',)
	ordering = ('-timestamp',)
	date_hierarchy = 'timestamp'
	list_filter = ('user',)

class TransactionAdmin(admin.ModelAdmin):
	list_display = ('user', 'info', 'credit', 'amount', 'total', 'date')
	date_hierarchy = 'date'
	list_filter = ('credit',)
	
class WithdrawalAdmin(admin.ModelAdmin):
	list_display = ('user', 'points', 'email', 'approved', 'date')
	date_hierarchy = 'date'
	list_filter = ('approved',)
	actions = [approve_withdrawals]
	
admin.site.register(UnitPack, UnitPackAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Withdrawal, WithdrawalAdmin)
