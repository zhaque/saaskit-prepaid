from django.contrib import admin
from models import UnitPack, Transaction

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
	
admin.site.register(UnitPack, UnitPackAdmin)
admin.site.register(Transaction, TransactionAdmin)
