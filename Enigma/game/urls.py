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
from django.conf import settings
from django.urls import path, include
from rest_framework.authtoken import views as tokenviews

from game import views, views2

"""
The commented path allow to have the library django.contrib.auth way to authenticate
"""
urlpatterns = [
    path('api/', views.archives, name='TheCircle'),

    path('api/detective/<int:id>/', views.DetectiveDetail.as_view()),

    # path('api/crime_location/<int:id>/', views.Crime_locationDetail.as_view()),
    # path('api/crime_locations/', views.Crime_locationList.as_view()),
    # path('api/filtered_crime_locations/', views2.Crime_locationList.as_view()),

    path('api/crime_detail/<int:id>/', views.Crime_detailsDetail.as_view()),
    path('api/crime_details/', views.Crime_detailsList.as_view()),
    path('api/filtered_crime_ldetails/', views2.Crime_detailsList.as_view()),

    path('api/record/<int:id>/', views.RecordDetail.as_view()),
    path('api/records/', views.RecordList.as_view()),
    path('api/filtered_records/', views2.RecordList.as_view()),

    path('api/insurance_owner/<int:id>/', views.InsuranceDetail.as_view()),
    path('api/insurance_owners/', views.InsuranceList.as_view()),
    path('api/filtered_insurance_owners/', views2.InsuranceList.as_view()),

    path('api/clue/<int:id>/', views.CluesDetail.as_view()),
    path('api/clues/', views.CluesList.as_view()),
    path('api/filtered_clues/', views2.CluesList.as_view()),

    path('api/killed/<int:id>/', views.KilledDetail.as_view()),
    path('api/killed/', views.KilledList.as_view()),
    path('api/filtered_killed/', views2.KilledList.as_view()),

    path('api/prisoners/<int:id>/', views.PrisonersDetail.as_view()),
    path('api/prisoners/', views.PrisonersList.as_view()),
    path('api/filtered_prisoners/', views2.PrisonersList.as_view()),

    path('api/quest/<int:id>/', views.QuestDetail.as_view()),

    path('api/mercenary/<int:id>/', views.MercenariesDetail.as_view()),
    path('api/mercenaries/', views.MercenariesList.as_view()),
    path('api/filtered_mercenaries/', views2.MercenariesList.as_view()),

    path('api/suspect/<int:id>/', views.SuspectDetail.as_view()),
    path('api/suspects/', views.SuspectList.as_view()),
    path('api/filtered_suspects/', views2.SuspectList.as_view()),

    path('api/victim/<int:id>/', views.VictimDetail.as_view()),
    path('api/victims/', views.VictimList.as_view()),
    path('api/filtered_victims/', views2.VictimList.as_view()),

    path('api-token-auth/', tokenviews.obtain_auth_token, name="api-token-auth"),
    path('registrate/', views.RegisterPage, name='registrate'),
    path('login/', views.LoginPage, name='login'),
    path('logout/', views.LoggedOutUser, name='logout'),
    path('home/', views.home, name='home'),
    # path('', include('django.contrib.auth.urls')),

]

####views2.py
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/victims/', views2.Victim_list),
#     path('api/victim/<int:id>/', views2.Victim_detail),
# ]
# urlpatterns += [
#     path('api-auth/', include('rest_framework.urls')),
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)
