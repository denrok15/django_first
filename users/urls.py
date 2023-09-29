from django.urls import path,include
from . import views
from .views import Register

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('vvedenie', views.vved, name='vved'),
    path('liney', views.liney, name='liney'),
    path('registr', views.registr, name='reg'),
    path('profile',views.profile,name='profile'),
    path('',include('django.contrib.auth.urls')),
    path('register/',Register.as_view(),name='register'),
    path('test',views.testir,name='test'),
    path('teor',views.teoria,name='teoria'),
    path('linteor',views.teorialin,name = 'linteor')


]
