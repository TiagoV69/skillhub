from django.urls import path
from . import views

app_name = 'habilidades'

urlpatterns = [
    path('', views.lista_habilidades, name='lista'),
    path('nueva/', views.crear_habilidad, name='crear'),
    path('<int:pk>/', views.detalle_habilidad, name='detalle'),
    path('<int:pk>/editar/', views.editar_habilidad, name='editar'),
    path('<int:pk>/eliminar/', views.eliminar_habilidad, name='eliminar'),
]
