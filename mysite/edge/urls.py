from django.conf.urls import url

from . import views

urlpatterns = [
    #/edge/characters/ = character index
    url(r'^characters/$', views.characterIndex, name='index'),

    #/edge/characters/id/ = specific character view
    url(r'^characters/(?P<character_id>[0-9]+)/$', views.getCharacter, name='character'),

    #/edge/characters/id/edit = edit specific character
    url(r'^characters/(?P<character_id>[0-9]+)/edit/$', views.editCharacter, name='edit')

]
