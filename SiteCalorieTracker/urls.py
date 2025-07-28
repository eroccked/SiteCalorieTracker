from django.contrib import admin
from django.urls import path, include
from myapp import views as myapp_views
from django.contrib.auth import views as auth_views

from django.shortcuts import render

def custom_404_view(request, exception):
    return render(request, '404.html', {}, status=404)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', myapp_views.register, name='register'),
    path('', myapp_views.index, name='index'),
    path('delete/<int:consume_id>/', myapp_views.delete_consume, name='delete_consume'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]


handler404 = custom_404_view