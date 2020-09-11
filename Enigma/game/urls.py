"""Enigma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
import rest_framework
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as tokenviews
from game.templates.registration import views as registrationviews

from game import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/suspect/<int:id>/', views.SuspectDetail.as_view()),
    path('api/suspects/', views.SuspectList.as_view()),
    path('api/victim/<int:id>/', views.VictimDetail.as_view()),
    path('api/victims/', views.VictimList.as_view()),
    path('api-token-auth/', tokenviews.obtain_auth_token),
    path('', include('django.contrib.auth.urls')),
    path('register/', registrationviews.register),
    # path('logout/', loginviews.auth_logout),

    # path('users/', views.UserList.as_view()),
    # path('user/<int:id>/', views.UserDetail.as_view()),
    # path('snippets/', views.SnippetList.as_view()),
    # path('snippets/<int:pk>/', views.SnippetDetail.as_view())
]
####views2.py
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/victims/', views2.Victim_list),
#     path('api/victim/<int:id>/', views2.Victim_detail),
# ]
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
# urlpatterns = format_suffix_patterns(urlpatterns)
