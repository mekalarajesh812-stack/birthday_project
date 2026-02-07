from django.urls import path
from .views import birthday_view,home_view,love

urlpatterns = [
    path('', home_view, name='home'),
    path('love/', love, name='love'),
    path('birthday/<int:id>/', birthday_view, name='birthday'),
]

