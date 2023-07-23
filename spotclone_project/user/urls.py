from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = (
    path('login/', views.LoginView.as_view() , name='user_login'),
    path('logout/', views.LogoutConfirmationView.as_view() , name='user_logout'),
    path('register/', views.RegisterView.as_view(), name='user_register'),
    path('details/', views.ProfileView.as_view(), name='user_details'),
    path('<int:pk>/update/', views.UserUpdateView.as_view(), name='user_update'),
    path('delete/<int:pk>', views.DeleteView.as_view(), name='user_delete'),
    
    # Password reset
    path('reset-password/', views.PasswordResetView.as_view(), name='reset_password'),
    # Email sent confirmation
    path('reset_password_sent/', views.PasswordResetDoneView.as_view(), name='reset_password_sent'),
    # Form for password change
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # Password Reset Complete
    path('reset_password_complete/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
)