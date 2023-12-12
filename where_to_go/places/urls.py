from django.urls import path

from . import views


urlpatterns = [
    path('', views.home_view),
    path('place/<int:place_id>/', views.place_view, name='place_view'),
]