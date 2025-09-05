from django.urls import path

from .views import cinema_list, cinema_detail

app_name = 'cinema'

urlpatterns = [
    path('', cinema_list, name='cinema_list'),
    path('<int:pk>/', cinema_detail, name='cinema_detail'),
]