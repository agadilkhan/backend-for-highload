from django.urls import path
from blog import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('hello_blog', views.hello_blog),

    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('post', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/create/', views.create_post, name='create_post'),
    path('post/<int:post_id>/edit/', views.edit_post, name='edit_post'),  
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),  
]