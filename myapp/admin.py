from django.contrib import admin
from .models import MenuItem,Order,OrderUpdate

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'section', 'price']
    list_filter = ['section']

admin.site.register(Order)

admin.site.register(OrderUpdate)