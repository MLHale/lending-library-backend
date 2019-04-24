# @Author: Matthew Hale <matthale>
# @Date:   2018-02-28T00:25:25-06:00
# @Email:  mlhale@unomaha.edu
# @Filename: urls.py
# @Last modified by:   matthale
# @Last modified time: 2018-03-02T02:50:46-06:00
# @Copyright: Copyright (C) 2018 Matthew L. Hale



from django.conf.urls import include, url

#Django Rest Framework
from rest_framework import routers

from api import controllers
from django.views.decorators.csrf import csrf_exempt

#REST API routes
router = routers.DefaultRouter(trailing_slash=False)
# router.register(r'users', controllers.UserViewSet)
# router.register(r'profiles', controllers.ProfileViewSet)
# router.register(r'awards', controllers.AwardViewSet)
router.register(r'users', controllers.UserViewSet)
router.register(r'userprofiles', controllers.UserProfileViewSet, base_name='userprofiles')
router.register(r'organizations', controllers.OrganizationViewSet, base_name='organizations')
# router.register(r'profiles', controllers.ProfileViewSet)
# router.register(r'stemfields', controllers.StemfieldViewSet)
# router.register(r'awardpurposes', controllers.AwardpurposeViewSet)
# router.register(r'areaofinterests', controllers.AreaofinterestViewSet)
# router.register(r'applicanttypes', controllers.ApplicanttypeViewSet)
# router.register(r'sources', controllers.SourceViewSet)
router.register(r'checkouts', controllers.CheckoutViewSet)
router.register(r'carts', controllers.CartViewSet, base_name='carts')
router.register(r'cartitemtypequantities', controllers.CartItemTypeQuantityViewSet, base_name='cartitemtypequantities')
#router.register(r'carts/(?P<pk>[^/.]+)/$', controllers.CartViewSet.as_view({'get': 'retrieve'}), name='cart-detail')
#router.register(r'carts/(?P<pk>[^/.]+)/(?P<related_field>\w+/$', controllers.CartViewSet.as_view({'get': 'retrieve_related'}), name='cart-related')
router.register(r'items', controllers.ItemViewSet)
# router.register(r'categories', controllers.CategoriesViewSet)

# Attempting ItemType communication with frontend
router.register(r'itemtypes', controllers.ItemTypeView, base_name='itemtypes')
router.register(r'packages', controllers.PackageView, base_name='packages')

urlpatterns = [
    url(r'^session', csrf_exempt(controllers.Session.as_view())),
    url(r'^register', csrf_exempt(controllers.Register.as_view())),
    url(r'^', include(router.urls)),
]
