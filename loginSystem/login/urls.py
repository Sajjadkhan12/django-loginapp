from django.urls import path,include
from django.contrib.auth import views as auth_views
from login import views as user_views
from . import views
urlpatterns = [
    path('',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('Dashboard/',views.dashboard,name='dashboard'),
    #path('password-reset/',views.password_reset,name='password_reset'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='login/password_reset.html'),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='login/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='login/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='login/password_reset_complete.html'),name='password_reset_complete'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='login/password_change.html'), 
        name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
        name='password_change_done'),
]