from django.urls import path
from django.contrib.auth import views
from users.views import RegisterFormView
app_name = 'users'
urlpatterns = [
    path('register/', RegisterFormView.as_view(), name="register"),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('password-reset/', views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'),
         name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
