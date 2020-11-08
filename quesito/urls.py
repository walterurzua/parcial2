from django.urls import path, include
from . import views 
from quesito.views import RegistroUsuario
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.inicio , name='inicio'),
    path('creaciondeusuarios', views.creaciondeusuarios , name='creaciondeusuarios'),
    path('registro', RegistroUsuario.as_view(), name='registro'),
    path('audifonos', views.audifonos , name='audifonos'),
    path('escritorio', views.escritorio , name='escritorio'),
    path('fuente', views.fuente , name='fuente'),
    path('monitor', views.monitor , name='monitor'),
    path('placa', views.placa , name='placa'),
    path('productos', views.productos , name='productos'),
    path('teclado', views.teclado , name='teclado'),
    path('lista', views.lista , name='lista'),
    path('accounts', include('django.contrib.auth.urls')),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
