# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib import admin
from django.utils.html import format_html

options = (('pending', 'pending'), ('processing', 'processing'), ('shipping', 'shipping'), ('cancel', 'cancel'))


class Banners(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=300, blank=True, null=True)
    banner_image = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'banners'


class Categories(models.Model):
    title = models.CharField(max_length=200)
    profile_photo = models.CharField(max_length=50)
    laundry = models.ForeignKey('Laundries', models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'categories'
        verbose_name_plural = 'categories'


class CustomerPromotions(models.Model):
    order = models.ForeignKey('Orders', models.DO_NOTHING)
    customer = models.ForeignKey('Customers', models.DO_NOTHING)
    promotion = models.ForeignKey('Promotions', models.DO_NOTHING)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customer_promotions'


class Customers(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=11)
    device_id = models.CharField(max_length=200)
    password = models.CharField(max_length=255)
    last_login_at = models.DateTimeField(blank=True, null=True)
    role = models.CharField(max_length=8)
    email_verification_code = models.CharField(max_length=6, blank=True, null=True)
    is_email_verified = models.CharField(max_length=1)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    jwt_token = models.TextField(blank=True, null=True)
    status_message = models.CharField(max_length=300, blank=True, null=True)
    profile_photo = models.CharField(max_length=50)
    customer_status = models.CharField(max_length=8)
    online_status = models.CharField(max_length=7)
    password_reset_code = models.CharField(max_length=6, blank=True, null=True)
    last_password_change_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customers'


class Items(models.Model):
    title = models.CharField(max_length=200)
    laundry = models.ForeignKey('Laundries', models.DO_NOTHING)
    category = models.ForeignKey(Categories, models.DO_NOTHING)
    ld = models.DecimalField(max_digits=10, decimal_places=2)
    dc = models.DecimalField(max_digits=10, decimal_places=2)
    pr = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'items'
        verbose_name_plural = 'Items'


class Laundries(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=11)
    profile_photo = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'laundries'


class Migrations(models.Model):
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class OrderItems(models.Model):
    order = models.ForeignKey('Orders', models.DO_NOTHING)
    item = models.ForeignKey(Items, models.DO_NOTHING)
    ld = models.DecimalField(max_digits=10, decimal_places=2)
    dc = models.DecimalField(max_digits=10, decimal_places=2)
    pr = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    service_type = models.CharField(max_length=2)

    class Meta:
        managed = False
        verbose_name_plural = 'order items'
        db_table = 'order_items'


class Orders(models.Model):
    laundry = models.ForeignKey(Laundries, models.DO_NOTHING)
    customer = models.ForeignKey(Customers, models.DO_NOTHING)
    order_title = models.CharField(max_length=200)
    expected_delivery_date = models.DateField(blank=True, null=True)
    customer_name = models.CharField(max_length=200)
    customer_phone = models.CharField(max_length=11)
    instruction = models.CharField(max_length=300)
    collection_address = models.CharField(max_length=300)
    delivery_address = models.CharField(max_length=300)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=100)

    order_status = models.CharField(max_length=10, choices=options)
    order_date = models.DateField()
    processing_date = models.DateField(blank=True, null=True)
    cancel_date = models.DateField(blank=True, null=True)
    shipping_date = models.DateField(blank=True, null=True)
    received_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'
        db_table = 'orders'
    def __str__(self):
        return 'Order No :'+str(self.id)
    @admin.display
    def last_activity(self):
        return self.updated_at

    @admin.display
    def email(self):
        return self.customer.email

    @admin.display
    def invoice(self):
        return format_html('<a href="/invoice/{}/">pdf</a>', self.id)

class Promotions(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300, blank=True, null=True)
    code = models.CharField(max_length=10)
    start_date = models.DateField()
    end_date = models.DateField()
    customer_limit = models.IntegerField()
    used_code = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'promotions'


class Reviews(models.Model):
    order = models.ForeignKey(Orders, models.DO_NOTHING)
    customer = models.ForeignKey(Customers, models.DO_NOTHING)
    review_status = models.CharField(max_length=9)
    comments = models.CharField(max_length=300, blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'reviews'
