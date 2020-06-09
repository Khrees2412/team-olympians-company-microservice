from django.urls import path
from . import views

urlpatterns = [
    path('',views.CompanyListCollection.as_view()),
    path("<int:pk>", views.CompanyListCollection.as_view())
]