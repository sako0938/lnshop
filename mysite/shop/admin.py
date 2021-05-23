from django.contrib import admin, messages

from .models import Product, Order, OrderItem
from lnd_pyshell.lnd_rest import *

# class OrderItemInline(admin.StackedInline):
# 	model = OrderItem

class OrderAdmin(admin.ModelAdmin):
	# inlines = [OrderItemInline,]
	list_display = ['order_uuid','sats_per_dollar','price_sats','ship_address','created_at','paid','shipped','payment_request']
	readonly_fields = ['items']
	actions = ['check_paid']

	def check_paid(self, request, queryset):
		newpaid = 0
		for i in queryset:
			pr = i.payment_request
			rhash = decodePR(pr)['payment_hash']
			paid = lookupInvoice(rhash)['settled']
			if paid:
				newpaid += 1
			i.paid = paid
			i.save()
		self.message_user(request,f'{newpaid} invoices have been paid!', messages.SUCCESS)

class OrderItemAdmin(admin.ModelAdmin):
	list_display = ['product','quantity']

class ProductAdmin(admin.ModelAdmin):
	list_display = ['name','description','supplier','price','product_image']

admin.site.register(Product,ProductAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem,OrderItemAdmin)