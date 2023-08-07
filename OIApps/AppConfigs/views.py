from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import views
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from AppConfigs.serializers import UserSerializer, GroupSerializer
from AppConfigs.models import App,Scope,Category
from AppConfigs.serializers import AppSerializer,CategorySerializer,ScopeSerializer
from django.conf import settings
from rest_framework import views
from rest_framework import status
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated
import numpy as np
import pandas as pd
import json
from pandas import json_normalize 
import logging
from dotenv import load_dotenv
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
import os
import requests
from requests.structures import CaseInsensitiveDict
import time
from AppConfigs.OiCache import OiCacheManager, OAuthManager
from django.http import HttpResponse
from django.http import JsonResponse
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
class AppsViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer    
    permission_classes = [permissions.IsAuthenticated]

class ScopeViewSet(viewsets.ModelViewSet):
    queryset = Scope.objects.all()
    serializer_class = ScopeSerializer
    permission_classes = [permissions.IsAuthenticated]


logging.basicConfig(
    format="%(thread)d - %(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)



class OIConnect(views.APIView):
  

    def post(self, request, format=None):
        load_dotenv()
        #logger = logging.getLogger(name="subscriber-to-oi-cache-api")
        resd = {}


        try:
            oauth_manager = OAuthManager()
            data = OiCacheManager().get_download_urls(oauth_manager.get_token, '105261').json()
            user = self.request.user
            print(user)
            #User.objects.filter(id=data['id']).update(email=data['email'], phone=data['phone'])

            Category.objects.filter(CreatedByUser=user).update(ResponseData = json.dumps(data))

            
            context = {
                  'Category': Category.objects.filter(CreatedByUser=user)  }
            return render (request, "data.html", context=context )
                                                        
                                                                                                          
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

       
    #         if 'ErrorDetail' in str(res):
    #             res = json.dumps({'data':data})
    #         else:
    #             res=json.dumps({'data':data})
    #     return render( res, data.html, {'response':res})
    # #except Exception as err:
        #reurn Response(str(err), status=status.HTTP_400_BAD_REQUEST)
 


def index(request):
# Render the HTML template index.html
    context = {
        'Category': Category.objects.all()
    }
    return render(request, 'home.html', context=context)