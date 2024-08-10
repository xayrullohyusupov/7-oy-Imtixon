from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_employee, name='create_employee'),
    path('update/<int:id>/', views.update_employee, name='update_employee'),
    path('delete/<int:id>/', views.delete_employee, name='delete_employee'),
    path('mark-attendance/<int:id>/', views.mark_attendance, name='mark_attendance'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('signup/', views.signup, name='signup'),
    path('api/',include('api.urls'), name='api'),
]
