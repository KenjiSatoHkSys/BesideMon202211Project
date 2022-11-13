from django.urls import path
from . import views

app_name = 'BesideMon202211'


urlpatterns = [
    # path('', views.index, name='index0'),
    path('logout', views.viewslogout, name='viewslogout'),
    path('', views.viewslogin, name='viewslogin'),
    path('index', views.index, name='index1'),
]
