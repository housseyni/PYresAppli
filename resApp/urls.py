
from django.urls import path
from . import views
from .views import create_evenement, lister_evenements

urlpatterns = [
    path('', views.index, name='index'),
    path('create_evenement/', create_evenement, name='create_evenement'),
    path('update/<int:evenement_id>/', views.update_evenement, name='update_evenement'),
    path('delete/<int:evenement_id>/', views.delete_evenement, name='delete_evenement'),
    path('list-evenements/', lister_evenements, name='lister_evenements'),
    path('evenements/', views.evenements, name='evenements'),
    path('add_evenement/', views.add_evenement, name='add_evenement'),
    path('edit_evenement/', views.edit_evenement, name='edit_evenement'),
    path('delete_evenement/', views.delete_evenement, name='delete_evenement'),
]
