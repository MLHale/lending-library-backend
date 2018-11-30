# @Author: Matthew Hale <matthale>
# @Date:   2018-02-28T00:25:25-06:00
# @Email:  mlhale@unomaha.edu
# @Filename: admin.py
# @Last modified by:   matthale
# @Last modified time: 2018-03-01T22:53:43-06:00
# @Copyright: Copyright (C) 2018 Matthew L. Hale



from django.contrib import admin

#if ENVIRONMENT == 'PROD':
#	from api.models import *
#else:
from api.models import *

# Register your models here.
admin.site.register(Award)
admin.site.register(Stemfield)
admin.site.register(Awardpurpose)
admin.site.register(Areaofinterest)
admin.site.register(Profile)
admin.site.register(Applicanttype)
admin.site.register(Source)
