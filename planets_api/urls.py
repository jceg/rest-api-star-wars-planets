from django.urls import path
from .views import PlanetListCreateView, PlanetRetrieveUpdateDeleteView

urlpatterns = [
    path('planets/', PlanetListCreateView.as_view(), name='planet-list-create'),
    path('planets/<int:pk>/', PlanetRetrieveUpdateDeleteView.as_view(), name='planet-retrieve-update-delete'),
]