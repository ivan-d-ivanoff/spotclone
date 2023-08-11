from django.urls import path, include, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = (
    path('login/', views.LoginView.as_view() , name='user_login'),
    path('logout/', views.LogoutConfirmationView.as_view() , name='user_logout'),
    path('register/', views.RegisterView.as_view(), name='user_register'),
    path('details/<int:pk>/', views.ProfileView.as_view(), name='user_details'),
    path('account/details/<int:pk>', views.OtherProfileView.as_view(), name='other_user_details'),  
    path('<int:pk>/update/', views.UserUpdateView.as_view(), name='user_update'),
    path('delete/<int:pk>/', views.DeleteView.as_view(), name='user_delete'),
    path('password-change/', views.ChangePasswordView.as_view(), name='user_password_change'),
)