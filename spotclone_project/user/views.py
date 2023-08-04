import os
from django.conf import settings
from django.contrib.auth import (
    views as auth_views,
    mixins as auth_mixins,
    get_user_model,
)
from django.contrib.auth import forms as auth_forms
from django.views import generic as views
from django.urls import reverse_lazy
from .models import Profile
from .forms import LoginForm, RegisterForm, DeleteUserForm, AddImageForm, UpdateProfileForm


User = get_user_model()

class LoginView(auth_views.LoginView):
    template_name = "user/login.html"
    form_class = LoginForm
    # redirect after login. Set to urlpattern name
    next_page = reverse_lazy("home")

class LogoutConfirmationView(auth_mixins.LoginRequiredMixin, views.TemplateView):
    template_name = 'user/logout.html'
     
    def get_redirect_field_name(self):
        return ''
    
    def post(self, request, *args, **kwargs):
        return auth_views.LogoutView.as_view(next_page=reverse_lazy('home'))(request, *args, **kwargs)

class RegisterView(views.CreateView):
    model = User
    template_name = "user/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("user_login")

    def form_valid(self, form):
        user = form.save()

        Profile.objects.create(user=user, 
                               email=user.email, 
                               username=user.username)

        return super().form_valid(form)


class ProfileView(auth_mixins.LoginRequiredMixin, views.TemplateView):
    template_name = "user/details.html"
    
    def get_redirect_field_name(self):
        return ''
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        profile = Profile.objects.filter(user=user).first()
        context["profile"] = profile
        context["form"] = AddImageForm()
        return context

class UserUpdateView(views.UpdateView):
    model = Profile
    form_class = UpdateProfileForm
    template_name = 'user/update.html'
    def get_success_url(self):
        return reverse_lazy('user_details', kwargs={'pk': self.request.user.pk})
    
    def get_object(self, queryset=None):
        # Return the Profile object based on the user's primary key
        return self.request.user.profile
    
    def form_valid(self, form):
        profile = form.save()
        return super().form_valid(form)
    
class DeleteView(views.DeleteView):
    model = User
    success_url = reverse_lazy("home")
    form_class = DeleteUserForm
    template_name = "user/delete.html"


class ChangePasswordView(auth_views.PasswordChangeView):
    template_name='user/password_change.html'
    
    def get_success_url(self):
        return reverse_lazy('user_details', kwargs={'pk': self.request.user.pk})