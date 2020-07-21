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
from rest_framework.validators import UniqueValidator
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator


class Profile(models.Model):
    # REGEX for phone number validation
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    
	UNL = 'unl'
	UNO = 'uno'
	UNMC = 'unmc'
	UNK = 'unk'
	OTHER = 'other'
	ORG_CHOICES = (
        (UNL, 'University of Nebraska - Lincoln'),
        (UNO, 'University of Nebraska - Omaha'),
        (UNMC, 'University of Nebraska Medical Center'),
        (UNK, 'University of Nebraska - Kearney'),
        (OTHER, 'Other'),
    )

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phonenumber = models.CharField(validators=[phone_regex], max_length=17, blank=False)
	address = models.CharField(max_length=254, blank=False)
	org = models.CharField(max_length=30, choices=ORG_CHOICES, default=UNO)

	def __str__(self):
		return str(self.user.username)
    
	class JSONAPIMeta:
		resource_name = "profiles"


class Checkout(models.Model):
    # REGEX for phone number validation
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    firstname = models.CharField(max_length=1000, blank=False)
    lastname = models.CharField(max_length=1000, blank=False)
    address = models.CharField(max_length=254, blank=False)
    email = models.CharField(max_length=100, blank=False)
    phonenumber = models.CharField(validators=[phone_regex], max_length=15, blank=False)
    numberofstudents = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)], blank=False)

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='checkouts', null=True, blank=True)

    createdon = models.DateTimeField(null=True, blank=True)
    fulfilledon = models.DateTimeField(null=True, blank=True)
    returnedon = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.lastname) + ', ' + str(self.firstname)

    class JSONAPIMeta:
        resource_name = "checkouts"

	class Meta:
		ordering = ['id']


class Category(models.Model):
    categoryname = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=1000, blank=False)
    image = models.ImageField(upload_to='img', blank=False)

    # Implicit fields
    # itemtypes

    def __str__(self):
        return str(self.categoryname)

    class Meta:
        verbose_name = "Category"
        ordering = ['-id']

    class JSONAPIMeta:
        resource_name = "categories"


class ItemType(models.Model):
    partname = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=1000, blank=False)
    category = models.ForeignKey(Category, related_name='itemtypes', on_delete=models.SET_NULL, null=True, blank=True, default=1)

    # Implicit fields
    # items

    def __str__(self):
        return str(self.partname)

    class Meta:
        verbose_name = "Item Type"
        ordering = ['-id']

    class JSONAPIMeta:
        resource_name = "itemtypes"


class Item(models.Model):
    itemtype = models.ForeignKey(ItemType, related_name='items', on_delete=models.CASCADE, default=1)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items', blank=False)
    checkedoutto = models.ForeignKey(Checkout, on_delete=models.SET_NULL, related_name='items', null=True, blank=True)
    missingpart = models.ForeignKey(Checkout, on_delete=models.SET_NULL, related_name='missingparts', null=True, blank=True)
    
    def __str__(self):
        return str(self.itemtype.partname)

    class Meta:
        verbose_name = "Item"
        ordering = ['-id']

    class JSONAPIMeta:
        resource_name = "items"

class UserSerializer(serializers.ModelSerializer):
    lastname = serializers.CharField(source='last_name')
    firstname = serializers.CharField(source='first_name')
    issuperuser = serializers.CharField(source='is_superuser')

    class Meta:
        resource_name = 'users'
        model = User
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    included_serializers = {
        'user': UserSerializer
    }

    class Meta:
        model = Profile
        fields = '__all__'

    class JSONAPIMeta:
        included_resources = ['user']

class CheckoutSerializer(serializers.ModelSerializer):

    class Meta:
        model = Checkout
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ItemTypeSerializer(serializers.ModelSerializer):
    included_serializers = {
        'category': CategorySerializer,
    }

    class Meta:
        model = ItemType
        fields = '__all__'

    class JSONAPIMeta:
        included_resources = ['category',]


class ItemSerializer(serializers.ModelSerializer):
    included_serializers = {
        'owner': UserSerializer,
        'checkedoutto': CheckoutSerializer,
      	'missingpart': CheckoutSerializer,
		'itemtype': ItemTypeSerializer,
    }

    class Meta:
        model = Item
        fields = '__all__'

    class JSONAPIMeta:
        included_resources = ['owner', 'itemtype', 'checkedoutto', 'missingpart']
