# @Author: Matthew Hale <matthale>
# @Date:   2018-02-28T00:25:25-06:00
# @Email:  mlhale@unomaha.edu
# @Copyright: Copyright (C) 2018 Matthew L. Hale
from django.contrib import admin
from api.models import *

# Register your models here.
admin.site.register(Profile)
admin.site.register(Item)
admin.site.register(ItemType)
admin.site.register(Category)
admin.site.register(Checkout)
