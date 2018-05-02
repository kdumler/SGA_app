from django.contrib import admin
from blog.models import Post, Item, RSO, Inventory_Check


class PostAdmin(admin.ModelAdmin):
    list_display = ('RSO', 'Description', 'date')
    search_fields = ['RSO', 'Description', 'date']


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'Tag_num', 'NOA_num', 'Item_name', 'Item_des', 'Manf_name', 'Model_num', 'Ser_num', 'Seller_name', 'Pur_date',
        'Pur_price', 'Warranty', 'War_end_date', 'Store_local', 'Store_add', 'Store_room', 'FOC_cat')

    search_fields = ['Tag_num', 'NOA_num', 'Item_name', 'Item_des', 'Manf_name', 'Model_num', 'Ser_num', 'Seller_name',
                     'Pur_date',
                     'Pur_price', 'Warranty', 'War_end_date', 'Store_local', 'Store_add', 'Store_room', 'FOC_cat']


class RSOAdmin(admin.ModelAdmin):
    list_display = ('RSO_name', 'RSO_prez', 'Prez_ph', 'Prez_email', 'RSO_advisor', 'Advisor_ph', 'Advisor_email')
    search_fields = ['RSO_name', 'RSO_prez', 'Prez_ph', 'Prez_email', 'RSO_advisor', 'Advisor_ph', 'Advisor_email']


class Inventory_CheckAdmin(admin.ModelAdmin):
    list_display = ('Tag_num', 'RSO_name', 'Curr_date', 'Condition', 'Retire_Date', 'Ck_Notes')
    search_fields = ['Tag_num', 'RSO_name', 'Curr_date', 'Condition', 'Retire_Date', 'Ck_Notes']


admin.site.register(Post, PostAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(RSO, RSOAdmin)
admin.site.register(Inventory_Check, Inventory_CheckAdmin)
