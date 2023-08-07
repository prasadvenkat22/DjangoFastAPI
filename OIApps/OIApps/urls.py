"""
URL configuration for OIApps project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""Secrets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from AppConfigs import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns


from django.contrib import admin
from django.urls import path, include
 
# Adds site header, site title, index title to the admin side.


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register('Apps', views.AppsViewSet)
router.register('Category', views.CategoryViewSet)
router.register('Scopes', views.ScopeViewSet)

 
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/OIConnect/', views.OIConnect.as_view()  ,name="OIConnect" ),
    path('', views.index, name='index'),

    #path('WriteToken/', views.CreateToken.as_view(),name="WriteToken"),
    #path('SecretsAPI/<int:pk>/', views.SecretsInfoDetail.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]

#urlpatt    path('OIConnect/', views.OIConnect.as_view()  ,name="OIConnect" ),
erns = format_suffix_patterns(urlpatterns)