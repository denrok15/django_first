from django.urls import path,include
from . import views
from .views import Register
from django.conf import settings
from django.conf.urls.static import static

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
    path('linteor',views.teorialin,name = 'vvodteor'),
    path('propety', views.properties, name='property'),
    path('grafic',views.grafics,name='grafic'),
    path('kyrsgraf',views.grafkyrs,name='grafkyrs'),
    path('parabola',views.parabola,name='parabola'),
    path('giperbola',views.giperbola,name='giperbola'),
    path('kx',views.kx,name='kx'),
    path('log',views.log,name='log'),
    path('trig',views.trig,name='trig'),
    path('bank',views.bank,name='bank'),
    path('kyrs2',views.kyrs2,name='kyrs2'),
    path('kyrs3',views.kyrs3,name='kyrs3'),
    path('kyrs4',views.kyrs4,name='kyrs4'),
    path('kyrs5',views.kyrs5,name='kyrs5'),
    path('lnteor',views.lnteor,name='lnteor'),
    path('lnprac',views.prln,name='lnprac'),
    path('grprac',views.grprac,name='grprac'),
    path('kvprac',views.kvprac,name='kvprace'),
    path('kvteor',views.kvteor,name='kvteor'),
    path('edit', views.edit_profile, name='edit'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
