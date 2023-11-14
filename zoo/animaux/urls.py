from django.urls import path
from . import views
from .views import index, decouvrir_animaux, animalerie,action

urlpatterns = [
    path('', index, name='index'),
    path('decouvrir_animaux', decouvrir_animaux, name='decouvrir_animaux'),
    path('animalerie', animalerie, name='animalerie'),
    path('action', action, name='action')

]
