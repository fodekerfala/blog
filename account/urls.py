from django.urls import path
from .views import connexion,inscription,deconnexion,recuperation,confirme

# app_name = 'accounts'
urlpatterns = [
    path('login',connexion,name='login'),
    path('inscription/',inscription,name='inscription'),
    path('logout/',deconnexion,name='deconnexion'),
    path('forgot/',recuperation,name='forgot'),
    path('confirm-password/<str:email>/',confirme,name='confirme_password')
]