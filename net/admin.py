from django.contrib import admin

from net.models import Provider, Contact, Product, Net


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Net)
class NetAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'provider', 'debt')
    list_filter = ('contact__city',)
    actions = ['clear_debt']

    def clear_debt(self, request, queryset):
        """
        Метод для очистки задолженности перед поставщиком.
        """
        for obj in queryset:
            obj.debt = 0
            obj.save()

    clear_debt.short_description = 'Очистить задолженность перед поставщиком'
