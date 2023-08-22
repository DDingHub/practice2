from django.urls import path
from . import views


urlpatterns = [
  path("character/", views.CharacterAPIView.as_view(), name="character"),
  path("myCharacter/", views.MyCharacterAPIView.as_view(), name="myCharacter")
]