from django.urls import path
from userapp import views
urlpatterns = [
    path('login/', views.user_Account),
]
