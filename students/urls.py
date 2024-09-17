from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/login/', permanent=False), name='root'),  # New line
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('home/', views.index, name='index'),
    path('<int:id>/', views.view_student, name='view_student'),
    path('add/', views.add, name='add'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('logout/', views.user_logout, name='logout'),
    path('delete/<int:id>/', views.delete, name='delete'),
]