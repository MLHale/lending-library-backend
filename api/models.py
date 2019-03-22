# @Author: Matthew Hale <matthale>
# @Date:   2018-02-28T00:25:25-06:00
# @Email:  mlhale@unomaha.edu
# @Filename: models.py
# @Last modified by:   matthale
# @Last modified time: 2018-03-05T14:15:06-06:00
# @Copyright: Copyright (C) 2018 Matthew L. Hale


from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from rest_framework_json_api import serializers
from django.core.validators import *

class Organization(models.Model):
	name = models.CharField(max_length=1000, blank=False)
	address1 = models.CharField(max_length=1000, blank=False)
	address2 = models.CharField(max_length=1000, blank=True)
	city = models.CharField(max_length=100, blank=False)
	state = models.CharField(max_length=2, blank=False)
	zipcode = models.CharField(max_length=20, blank=False)

	def __str__(self):
		return self.name

ADMIN = 'ADM'
LENDER = 'LEN'
USER_ROLE_CHOICES = (
	(ADMIN,'Admin'),
	(LENDER, 'Lender'),
)
class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	org = models.ForeignKey(Organization, blank=False)
	roles = models.TextField(max_length=200, blank=True, choices=USER_ROLE_CHOICES)

	def __str__(self):
		return self.user.username



class ItemType(models.Model):
	name = models.CharField(max_length=200, blank=False)
	description = models.TextField(max_length=1000, blank=True)
	imagepath = models.TextField(max_length=200, blank=False, default="notfound.jpg")

	def __str__(self):
		return self.name

class Cart(models.Model):
	user = models.ForeignKey(UserProfile, blank=False)
	items = models.ManyToManyField(
		ItemType,
		through='CartItemTypeRel',
		through_fields=('cart', 'itemtype'),
	)

	def __str__(self):
		return "Cart: %s" % self.user

class CartItemTypeRel(models.Model):
	cart = models.ForeignKey(Cart, blank=False)
	itemtype = models.ForeignKey(ItemType, blank=False)
	quantity = models.PositiveIntegerField(blank=True, default=1)

	def __str__(self):
		return "Cart: %s -> ItemType: %s" % (self.cart.id, self.itemtype)


AVAIL = 'AVA'
CO = 'CO'
BROKE = 'BRO'
MISSING = 'MIS'
NOTRET = 'NOR'
ITEM_STATUS_CHOICES = (
	(AVAIL, 'Available'),
	(CO,'Checked Out'),
	(BROKE, 'Broken'),
	(MISSING, 'Missing'),
	(NOTRET, 'Not Returned'),
)

class Item(models.Model):
	type = models.ForeignKey(ItemType, blank=False, default=1)
	barcode = models.CharField(max_length=100, blank=True)
	status = models.CharField(max_length=100, blank=False, choices=ITEM_STATUS_CHOICES, default=AVAIL )
	owner = models.ForeignKey(UserProfile, blank=False)
	checkedoutto = models.ForeignKey(UserProfile, null=True, related_name='items')

	def __str__(self):
		return "Item: %s ID: %s" % (self.type, self.id)

class History(models.Model):
	user = models.ForeignKey(UserProfile, blank=False)
	items = models.ManyToManyField(Item, blank=False)
	createdon = models.DateTimeField(null=True, blank=True)
	fulfilledon = models.DateField(null=True, blank=True)
	returnedon = models.DateField(null=True, blank=True)
	missingparts = models.TextField(max_length=1000, blank=True)

	def __str__(self):
		return "History ID:%s User: %s Returned: %s" % (self.id, self.user, self.returnedon)


#class HistoryItemRel(models.Model):
#	history = models.ForeignKey(History, blank=False)
#	item = models.ForeignKey(Item, related_name='items', blank=False)
#
#	def __str__(self):
#		return "History: %s -> Item: %s" % (self.history, self.item)

ORDERED = 'ORD'
INFUL = 'INFUL'
FUL = 'FUL'
SHIPPED = 'SHIP'
RECEIVED = 'REC'
ORDER_STATUS_CHOICES = (
	(ORDERED,'Ordered'),
	(INFUL, 'In Fulfillment'),
	(FUL, 'Fulfilled'),
	(SHIPPED, 'Shipped'),
	(RECEIVED, 'Return Received'),
)

class Order(models.Model):
	user = models.ForeignKey(UserProfile, blank=False)
	status = models.CharField(max_length=100, blank=False, choices=ORDER_STATUS_CHOICES )
	items = models.ManyToManyField(Item, blank=False)
	createdon = models.DateTimeField(null=True, blank=True)
	fulfilledon = models.DateField(null=True, blank=True)
	returnedon = models.DateField(null=True, blank=True)
	missingparts = models.TextField(max_length=1000, blank=True)

	def __str__(self):
		return "Order ID:%s" % self.id

# class OrderItemsRel(models.Model):
#      order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=False)
#      item = models.ForeignKey(Item, related_names='items', blank=False)

class Package(models.Model):
	name = models.CharField(max_length=200, blank=False)
	description = models.TextField(max_length=1000, blank=False)
	items = models.ManyToManyField(
		ItemType,
		through='PackageItemTypeRel',
		through_fields=('package', 'itemtype'),
	)

	def __str__(self):
		return self.name


class PackageItemTypeRel(models.Model):
	package = models.ForeignKey(Package, blank=False)
	itemtype = models.ForeignKey(ItemType, blank=False)
	quantity = models.PositiveIntegerField(blank=True, default=1)

	def __str__(self):
		return "Package: %s -> ItemType: %s" % (self.package, self.itemtype)


class OrganizationSerializer(serializers.ModelSerializer):
        class Meta:
                model = Organization
                fields = ('id','name','address1','address2','city','state','zip')

class UserProfileSerializer(serializers.ModelSerializer):
        class Meta:
                model = UserProfile
                fields = ('id','username','first_name','last_name','email','password','user_permissions', 'is_superuser','is_active', 'last_login',
'date_joined', 'org')

class OrderSerializer(serializers.ModelSerializer):
        class Meta:
                model = Order
                fields = ('id','user','status','createdon','fulfilledon','returndon','missingpars')

class ItemTypeSerializer(serializers.ModelSerializer):
        class Meta:
                model = ItemType
                fields = ('id','name','description')

class ItemSerializer(serializers.ModelSerializer):
        class Meta:
                model = Item
                fields = ('id','type','barcode', 'status', 'owner', 'order', 'checkedoutto')

class PackageSerializer(serializers.ModelSerializer):
        class Meta:
                model = Package
                fields = ('id','name','description', 'items')

class PackageItemTypeRelSerializer(serializers.ModelSerializer):
        class Meta:
                model = PackageItemTypeRel
                fields = ('id','package','itemtype', 'quantity')
