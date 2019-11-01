from django.urls import path

from . import views

app_name = 'pages'
urlpatterns = [
    path('origin/', views.index, name='index'),
    path('', views.test)
    ]