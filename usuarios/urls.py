from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('', views.lista_usuarios, name='lista'),
    path('nuevo/', views.crear_usuario, name='crear'),
    path('<int:pk>/', views.detalle_usuario, name='detalle'),
    path('<int:pk>/editar/', views.editar_usuario, name='editar'),
    path('<int:pk>/eliminar/', views.eliminar_usuario, name='eliminar'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('callback', views.callback, name='callback'),
    path('auth-home', views.index, name='index'),
]
