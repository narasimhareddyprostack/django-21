from django.urls import path
from savingsapp import views
urlpatterns = [
    path('id/', views.saving_Account),
]
