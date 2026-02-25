from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('submit/<int:assignment_id>/', views.submit_assignment_view, name='submit'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.login_view, name='index'),
]
