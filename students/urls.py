from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.landing, name='home'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('dashboard/', views.index, name='dashboard'),  # Changed name from 'index' to 'dashboard'
    path('<int:id>/', views.view_student, name='view_student'),
    path('add/', views.add, name='add'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('logout/', views.user_logout, name='logout'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('register/', views.register, name='register'),
]