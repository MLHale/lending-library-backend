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
	"""
	This model is connected to a UserProfile to define Organization and address
	information.
	"""
	name = models.CharField(max_length=1000, blank=False)
	address1 = models.CharField(max_length=1000, blank=False)
	address2 = models.CharField(max_length=1000, blank=True)
	city = models.CharField(max_length=100, blank=False)
	state = models.CharField(max_length=2, blank=False)
	zipcode = models.CharField(max_length=20, blank=False)

	class JSONAPIMeta:
		resource_name = "organizations"

	def __str__(self):
		return self.name

class UserProfile(models.Model):
	"""
	This model allows a User to have an Organization and isadmin/islender flags.
	"""
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	org = models.ForeignKey(Organization, blank=False)
	isadmin = models.BooleanField(default=False)
	islender = models.BooleanField(default=False)

	class JSONAPIMeta:
		resource_name = "userprofiles"

	def __str__(self):
		return self.user.username

class ItemType(models.Model):
	"""
	This model classifies an instance of the Item model. It provides a name,
	description, and a path to an image.
	"""
	name = models.CharField(max_length=200, blank=False)
	description = models.TextField(max_length=1000, blank=True)
	imagepath = models.TextField(
		max_length=200,
		blank=False,
		default="notfound.jpg"
		)

	class JSONAPIMeta:
		resource_name = "itemtypes"

	def __str__(self):
		return self.name

class Cart(models.Model):
	"""
	This model allows a user to have a Cart. It can contain items that the User
	selects from the Lending Library.
	"""
	user = models.ForeignKey(UserProfile, blank=False)

	# Implicit Fields
	# cartitemtypequantities

	class JSONAPIMeta:
		resource_name = "carts"

	def __str__(self):
		return "Cart: %s" % self.user

class CartItemTypeQuantity(models.Model):
	"""
	This model allows a Cart to contain different ItemTypes of varying
	quantities.
	"""
	cart = models.ForeignKey(Cart,
		blank=False,
		related_name="cartitemtypequantities",
		on_delete=models.CASCADE)
	itemtype = models.ForeignKey(ItemType,
		blank=False,
		on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(blank=True, default=1)

	class JSONAPIMeta:
		resource_name = "cartitemtypequantities"

	def __str__(self):
		return "%s -> ItemType: %s -> Quantity: %s" \
			% (self.cart, self.itemtype, self.quantity)

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
	"""
	This model defines an instance of a real-world Item placed within the
	database.
	"""
	type = models.ForeignKey(ItemType, blank=False, default=1)
	barcode = models.CharField(max_length=100, blank=True)
	status = models.CharField(
		max_length=100,
		blank=False,
		choices=ITEM_STATUS_CHOICES,
		default=AVAIL
		)
	owner = models.ForeignKey(UserProfile, blank=False)
	checkedoutto = models.ForeignKey(
		UserProfile,
		blank=True,
		null=True,
		related_name='items'
		)

	class JSONAPIMeta:
		resource_name = "items"

	def __str__(self):
		return "Item: %s ID: %s" % (self.type, self.id)

class History(models.Model):
	"""
	A completed Order model will be migrated to a History model. This is done to
	maintain a manageable Order table size for faster queries.
	"""
	user = models.ForeignKey(UserProfile, blank=False)
	items = models.ManyToManyField(Item, blank=False)
	createdon = models.DateTimeField(null=True, blank=True)
	fulfilledon = models.DateField(null=True, blank=True)
	returnedon = models.DateField(null=True, blank=True)
	missingparts = models.TextField(max_length=1000, blank=True)

	class JSONAPIMeta:
		resource_name = "histories"

	def __str__(self):
		return "History ID: %s User: %s Returned: %s" % (
			self.id,
			self.user,
			self.returnedon
			)

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
	"""
	This model tracks the items that a User has borrowed until the items are
	returned.
	"""
	user = models.ForeignKey(UserProfile, blank=False)
	status = models.CharField(
		max_length=100,
		blank=False,
		choices=ORDER_STATUS_CHOICES
		)
	items = models.ManyToManyField(Item, blank=False)
	createdon = models.DateTimeField(null=True, blank=True)
	fulfilledon = models.DateField(null=True, blank=True)
	returnedon = models.DateField(null=True, blank=True)
	missingparts = models.TextField(max_length=1000, blank=True)

	class JSONAPIMeta:
		resource_name = "orders"

	def __str__(self):
		return "Order ID: %s" % self.id

class Package(models.Model):
	"""
	This model allows Users to add a set of Items, defined by this model, to
	their Cart.
	"""
	name = models.CharField(max_length=200, blank=False)
	description = models.TextField(max_length=1000, blank=False)

	# Implicit Fields
	# packageitemtypequantities

	class JSONAPIMeta:
		resource_name = "packages"

	def __str__(self):
		return self.name

class PackageItemTypeQuantity(models.Model):
	"""
	This model enables the Package model to contain various quantities of
	multiple ItemTypes.
	"""
	package = models.ForeignKey(Package,
		blank=False,
		related_name="packageitemtypequantities",
		on_delete=models.CASCADE)
	itemtype = models.ForeignKey(ItemType,
		blank=False,
		on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(blank=True, default=1)

	class JSONAPIMeta:
		resource_name = "packageitemtypequantities"

	def __str__(self):
		return "Package: %s -> ItemType: %s -> Quantity: %s" \
			% (self.package, self.itemtype, self.quantity)

# Begin Serializers

class OrganizationSerializer(serializers.ModelSerializer):
	"""
	Allows for serialization and deserialization of the Organization model.
	"""
	class Meta:
		model = Organization
		fields = (
			'id',
			'name',
			'address1',
			'address2',
			'city',
			'state',
			'zipcode'
			)

class UserProfileSerializer(serializers.ModelSerializer):
	"""
	Allows for serialization and deserialization of the UserProfile model.
	"""
	included_serializers = {
		'org': OrganizationSerializer,
	}

	class Meta:
		model = UserProfile
		fields = (
			'id',
			'org',
			'isadmin',
			'islender'
			)

	class JSONAPIMeta:
		included_resources = ['org',]

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = (
			'username',
			'email'
		)

class ItemTypeSerializer(serializers.ModelSerializer):
	"""
	Allows for serialization and deserialization of the ItemType model.
	"""
	class Meta:
		model = ItemType
		fields = ('id', 'name', 'description', 'imagepath')

class CartItemTypeQuantitySerializer(serializers.ModelSerializer):
	"""
	Allows for serialization and deserialization of the CartItemTypeRel model.
	"""
	class Meta:
		model = CartItemTypeQuantity
		fields = ('id', 'cart', 'itemtype', 'quantity')

class CartSerializer(serializers.ModelSerializer):
	"""
	Allows for serialization and deserialization of the Cart model.
	"""
	included_serializers = {
		'cartitemtypequantities': CartItemTypeQuantitySerializer,
	}

	class Meta:
		model = Cart
		fields = ('id', 'user', 'cartitemtypequantities')

	class JSONAPIMeta:
		included_resources = ['cartitemtypequantities']

class ItemSerializer(serializers.ModelSerializer):
	"""
	Allows for serialization and deserialization of the Item model.
	"""
	class Meta:
		model = Item
		fields = (
		'id',
		'type',
		'barcode',
		'status',
		'owner',
		'checkedoutto'
		)

class HistorySerializer(serializers.ModelSerializer):
	"""
	Allows for serialization and deserialization of the History model.
	"""
	class Meta:
		model = History
		fields = (
		'id',
		'user',
		'items',
		'createdon',
		'fulfilledon',
		'returnedon',
		'missingparts'
		)

class OrderSerializer(serializers.ModelSerializer):
	"""
	Allows for serialization and deserialization of the Order model.
	"""
	class Meta:
		model = Order
		fields = (
		'id',
		'user',
		'status',
		'items',
		'createdon',
		'fulfilledon',
		'returnedon',
		'missingparts'
		)

class PackageItemTypeQuantitySerializer(serializers.ModelSerializer):
	"""
	Allows for serialization and deserialization of the PackageItemTypeQuantity
	model.
	"""
	class Meta:
		model = PackageItemTypeQuantity
		fields = ('id', 'package', 'itemtype', 'quantity')

class PackageSerializer(serializers.ModelSerializer):
	"""
	Allows for serialization and deserialization of the Package model.
	"""
	included_serializers = {
		'packageitemtypequantities': PackageItemTypeQuantitySerializer,
	}

	class Meta:
		model = Package
		fields = ('id', 'name', 'description', 'packageitemtypequantities')

	class JSONAPIMeta:
		included_resources = ['packageitemtypequantities']
