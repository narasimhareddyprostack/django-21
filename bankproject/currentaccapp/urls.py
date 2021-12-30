from django.urls import path
from currentaccapp import views
urlpatterns = [
    path('login/', views.current_Account),
]
