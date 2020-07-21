# @Author: Matthew Hale <matthale>
# @Date:   2018-02-28T00:25:25-06:00
# @Email:  mlhale@unomaha.edu
# @Filename: controllers.py
# @Last modified by:   matthale
# @Last modified time: 2018-03-02T04:06:42-06:00
# @Copyright: Copyright (C) 2018 Matthew L. Hale


# Handy Django Functions
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login, logout
import datetime
import pytz

# Models and serializers
from django.contrib.auth.models import User
import api.models as api

# REST API Libraries
from rest_framework import viewsets, parsers, renderers
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import list_route
from rest_framework.authentication import *

from rest_framework.parsers import JSONParser

# Email
from templated_email import send_templated_mail


from api.pagination import *

from django.core import serializers
from django.core.exceptions import ValidationError
from api.models import Item
from api.models import ItemType
from api.models import Category
from django.db.models import Count

import bleach
import time

# For category Image
import base64
from django.core.files.base import ContentFile


def home(request):
    """
    Send requests to '/' to the ember.js clientside app
    """

    return render(request, 'index.html')


def staff_or_401(request):
    if not request.user.is_staff:
        return Response({'success': False}, status=status.HTTP_401_UNAUTHORIZED)


def super_user_or_401(request):
    if not request.user.is_superuser:
        return Response({'success': False}, status=status.HTTP_401_UNAUTHORIZED)


def admin_or_401(request):
    if not (request.user.is_staff or request.user.is_superuser):
        return Response({'success': False}, status=status.HTTP_401_UNAUTHORIZED)


class CheckoutViewSet(viewsets.ModelViewSet):
    """
    Endpoint that loads the people checking out the Items
    """
    permission_classes = (AllowAny,)
    resource_name = 'checkouts'
    queryset = api.Checkout.objects.all()
    serializer_class = api.CheckoutSerializer
    filter_fields = ('id', 'firstname', 'lastname', 'profile', 'createdon', 'fulfilledon', 'returnedon')

    def create(self, request):
        serializer = api.CheckoutSerializer(data=request.data)
        if serializer.is_valid():
            checkout = serializer.save()
            
            # TODO: Add order information to email
            # TODO: It doesnt work because the patch request to items goes out after checkout is saved and email goes out on checkout save

            # Send order placed email
            send_templated_mail(
                template_name='order-placed',
                from_email='unolendinglibrary@gmail.com',
                recipient_list=[request.data.get('email')],
                context={
                    'account': (request.data.get('profile') is not None),
                    'ordernumber': checkout.id,
                    'domain': 'http://localhost/'
                },
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        admin_or_401(request)

        # Get the checkout before it updates to check differences
        checkout = api.Checkout.objects.get(pk=request.data.get('id'))

        if checkout.fulfilledon == None and request.data.get('fulfilledon') is not None:
            # The order was just fulfilled
            # Send order fulfilled email
            send_templated_mail(
                template_name='order-fulfilled',
                from_email='unolendinglibrary@gmail.com',
                recipient_list=[checkout.email],
                context={
               		'ordernumber': checkout.id,
                },
            )

        if checkout.returnedon == None and request.data.get('returnedon') is not None:
            # The order was just returned
            # Send order fulfilled email
            send_templated_mail(
                template_name='order-returned',
                from_email='unolendinglibrary@gmail.com',
                recipient_list=[checkout.email],
                context={
					'ordernumber': checkout.id,
                },
            )

        serializer = self.get_serializer(self.get_object(), data=request.data, partial=kwargs.pop('partial', False))
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ItemViewSet(viewsets.ModelViewSet):
    """
    Endpoint to view the items
    """
    resource_name = 'items'
    serializer_class = api.ItemSerializer
    queryset = api.Item.objects.all()
    permission_classes = (AllowAny,)
    filter_fields = ('id', 'itemtype', 'owner', 'checkedoutto', 'missingpart')

    def create(self, request, *args, **kwargs):
        admin_or_401(request)

        serializer = api.ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        admin_or_401(request)

        serializer = self.get_serializer(self.get_object(), data=request.data, partial=kwargs.pop('partial', False))
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False)
    def count(self, request):
        owner = api.User.objects.get(pk=request.data.get('owner').get('id'))
        items = Item.objects.all().filter(owner=owner)
        countitems = items.aggregate(Count('owner'))
        return Response({'count': countitems})


class ItemTypeViewSet(viewsets.ModelViewSet):
    """
    Endpoint to view the itemtypes
    """
    resource_name = 'itemtypes'
    serializer_class = api.ItemTypeSerializer
    queryset = api.ItemType.objects.all()
    permission_classes = (AllowAny,)
    filter_fields = ('id', 'partname', 'description', 'category', 'items',)

    def create(self, request, *args, **kwargs):
        admin_or_401(request)

        serializer = api.ItemTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def update(self, request, *args, **kwargs):
        admin_or_401(request)

        serializer = self.get_serializer(self.get_object(), data=request.data, partial=kwargs.pop('partial', False))
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False)
    def count(self, request):
        partname = self.request.query_params.get('partname', None)
        items = ItemType.objects.all().filter(partname=partname)
        countitems = items.aggregate(Count('partname'))
        return Response({'count': countitems})

import json
class CategoriesViewSet(viewsets.ModelViewSet):
    """
    Endpoint to view the categories
    """
    resource_name = 'categories'
    serializer_class = api.CategorySerializer
    queryset = api.Category.objects.all()
    permission_classes = (AllowAny,)
    filter_fields = ('id', 'categoryname', 'description')

    def create(self, request, *args, **kwargs):
        admin_or_401(request)

        format, imgstr = request.data.get('image').split(';base64,')
        ext = format.split('/')[-1]
        imageFile = ContentFile(base64.b64decode(imgstr), name=(request.data.get('categoryname') + '.' + ext))

        newCategory = Category(
            categoryname=request.data.get('categoryname'),
            description=request.data.get('description'),
            image=imageFile
        )
        try:
            newCategory.clean_fields()
        except ValidationError as e:
            print(e)
            print(str(request.data.get('categoryname')))
            print(str(request.data.get('description')))
            print(str(request.data.get('image')))
            return Response({'success': False, 'error': e}, status=status.HTTP_400_BAD_REQUEST)

        newCategory.save()
        category = Category.objects.filter(pk=newCategory.id).values('categoryname', 'description', 'image')
        data = {"type": "categories", "id": str(newCategory.id), "attributes": category[0]}
        return Response(data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        admin_or_401(request)

        serializer = self.get_serializer(self.get_object(), data=request.data, partial=kwargs.pop('partial', False))
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False)
    def count(self, request):
        categoryname = self.request.query_params.get('categoryname', None)
        categories = Category.objects.all().filter(categoryname=categoryname)
        countitems = categories.aggregate(Count('categoryname'))
        return Response({'count': countitems})


class UserViewSet(viewsets.ModelViewSet):
    """
    Endpoint that allows user data to be viewed.
    """
    resource_name = 'users'
    serializer_class = api.UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return User.objects.all()
        return User.objects.filter(username=user.username)

    def update(self, request, *args, **kwargs):
        user = User.objects.get(pk=request.data.get('id'))
        user.first_name = request.data.get('firstname')
        user.last_name = request.data.get('lastname')
        user.email = request.data.get('email')
        saved = user.save(update_fields=['first_name', 'last_name', 'email'])

        return Response(saved, status=status.HTTP_200_OK)
    
class ProfileViewSet(viewsets.ModelViewSet):
    """
    Endpoint that allows user data to be viewed.
    """
    resource_name = 'profiles'
    serializer_class = api.ProfileSerializer
    queryset = api.Profile.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return api.Profile.objects.all()
        return api.Profile.objects.filter(user__username=user.username)


class Register(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        # Login
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
    
        if username is not None and password is not None and email is not None:
			lastname = request.POST.get('lastname')
			firstname = request.POST.get('firstname')
			address = request.POST.get('address')
			phone = request.POST.get('phone')
			org = request.POST.get('org')
			
			if User.objects.filter(username=username).exists():
				return Response({'msg': 'Username is taken.', 'status': 'error'})
			elif User.objects.filter(email=email).exists():
				return Response({'msg': 'Email is taken.', 'status': 'error'})

            # especially before you pass them in here
			newuser = User.objects.create_user(email=bleach.clean(email), username=bleach.clean(username), password=password, last_name=bleach.clean(
                lastname), first_name=bleach.clean(firstname))

			newprofile = api.Profile(
                user=newuser, address=bleach.clean(address), phonenumber=bleach.clean(phone), org=bleach.clean(org))

			newprofile.save()

			# This is so we can display the full organization name in the email
			organizations = {
				'unl': 'University of Nebraska - Lincoln',
				'uno': 'University of Nebraska - Omaha',
				'unmc': 'University of Nebraska Medical Center',
				'unk': 'University of Nebraska - Kearney',
				'other': 'Other',
			}

            # Send welcome email
			send_templated_mail(
                template_name='welcome',
                from_email='unolendinglibrary@gmail.com',
                recipient_list=[email],
                context={
                    'email': email,
					'username': username,
					'firstname': firstname,
					'fullname': (firstname + ' ' + lastname),
					'phone': phone,
					'org': organizations[org],
					'domain': 'http://localhost/'
                },
                # Optional:
                # cc=['cc@example.com'],
                # bcc=['bcc@example.com'],
            )

			user = authenticate(username=bleach.clean(username), password=password)
			login(request, user)
			
			return Response({'status': 'success', 'userid': newuser.id, 'profile': newprofile.id})
        else:
            return Response({'status': 'error', 'msg': 'You must fill in all the form fields.'})


class Session(APIView):
    """
    Returns a JSON structure: {'isauthenticated':<T|F>,'userid': <int:None>,'username': <string|None>,'profileid': <int|None>}
    """
    permission_classes = (AllowAny,)

    def form_response(self, isauthenticated, userid, username, profileid, error=""):
        data = {
            'isauthenticated': 	isauthenticated,
                'userid': 			userid,
                'username': 		username,
                'profileid':		profileid,
        }
        if error:
            data['message'] = error

        return Response(data)

    def get(self, request, *args, **kwargs):
        # Get the current user
        user = request.user
        if user.is_authenticated():
            profile = get_object_or_404(api.Profile, user__username=user.username)
            return self.form_response(True, user.id, user.username, profile.id)
        return self.form_response(False, None, None, None)

    def post(self, request, *args, **kwargs):
        # Login
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=bleach.clean(username), password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                profile = get_object_or_404(api.Profile, user__username=user.username)
                return self.form_response(True, user.id, user.username, profile.id)
            return self.form_response(False, None, None, None, "Account is suspended")
        return self.form_response(False, None, None, None, "Invalid username or password")

    def delete(self, request, *args, **kwargs):
        # Logout
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)
