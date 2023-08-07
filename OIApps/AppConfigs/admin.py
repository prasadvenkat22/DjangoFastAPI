from django.contrib import admin
from .models import Category,App,Scope
# Register your models here.
admin.site.register(App)
admin.site.register(Category)
admin.site.register(Scope)


# Adds site header, site title, index title to the admin side.
admin.site.site_header = 'UP OI Cache Admin Page'
admin.site.site_title = 'Pass-through OI Configs'
admin.site.index_title = 'Config'