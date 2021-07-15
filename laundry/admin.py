from django.contrib import admin
from django.contrib.auth.models import Group

from laundry.models import Orders, Categories, Items, OrderItems


@admin.action(description='Mark selected orders as processing')
def make_processing(modeladmin, request, queryset):
    queryset.update(order_status='processing')


@admin.action(description='Mark selected orders as shipping')
def make_shipping(modeladmin, request, queryset):
    queryset.update(order_status='shipping')


@admin.action(description='Mark selected orders as cancel')
def make_cancel(modeladmin, request, queryset):
    queryset.update(order_status='cancel')


# @admin.action(description='Mark selected orders as shipped')
# def make_shipped(modeladmin, request, queryset):
#     queryset.update(order_status='shipped')

admin.site.index_title = ''
admin.site.site_header = 'Dashboard'
admin.site.site_title = 'Admin'


class CustomOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'email', 'last_activity', 'order_status','invoice')
    list_display_links = ('customer_name', 'email',)
    search_fields = ('customer_name', 'customer_phone',)
    save_on_top = True
    list_filter = ('order_date',)
    list_editable = ('order_status',)
    actions = [make_processing, make_shipping, make_cancel]


admin.site.register(Orders, CustomOrderAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('title',)
    save_on_top = True


admin.site.register(Categories, CategoryAdmin)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('title',)
    save_on_top = True


admin.site.register(Items, ItemAdmin)
admin.site.register(OrderItems)
admin.site.unregister(Group)
