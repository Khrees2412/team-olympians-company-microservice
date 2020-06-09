from django.contrib import admin
from django.urls import path, include
from comservices import views
'''
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Team Olympians",
      
   ),
    path('', schema_view ),
   url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('comservices/', include('comservices.urls')),

]