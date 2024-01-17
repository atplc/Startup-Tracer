from django.urls import path
from . import views

urlpatterns = [
    path('',views.StartupTracer.as_view()),
]
