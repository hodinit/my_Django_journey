"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.urls import path
from django.shortcuts import redirect

from boards import views
from accounts import views as accounts_views

def custom_logout(request):
    logout(request)
    return redirect('home')

urlpatterns = [
    path('', views.BoardListView.as_view(), name='home'),
    path('signup/', accounts_views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', custom_logout, name='logout'),
    path('admin/', admin.site.urls),

    path('boards/<int:pk>/', views.TopicListView.as_view(), name='board_topics'),
    path('boards/<int:pk>/new', views.new_topic, name= 'new_topic'),
    path('boards/<int:pk>/topics/<int:topic_pk>/', views.PostListView.as_view(), name='topic_posts'),
    path('boards/<int:pk>/topics/<int:topic_pk>/reply/', views.reply_topic, name='reply_topic'),
    path('boards/<int:pk>/topics/<int:topic_pk>/posts/<int:post_pk>/edit/', 
        views.PostUpdateView.as_view(), name='edit_post'),

    path('reset/', 
        auth_views.PasswordResetView.as_view(
            template_name ='password_reset.html',
            email_template_name = 'password_reset_email.html',
            subject_template_name = 'password_reset_subject.txt'
        ),
        name = 'password_reset'),
    path('reset/done/', 
        auth_views.PasswordResetDoneView.as_view(template_name = 'password_reset_done.html'),
        name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name = 'password_reset_confirm'),
    path('reset/complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name = 'password_reset_complete.html'),
        name = 'password_reset_complete'),

    path('settings/password/', auth_views.PasswordChangeView.as_view(template_name = 'password_change.html'),
        name = 'password_change'),
    path('settings/password/done/', auth_views.PasswordChangeDoneView.as_view(template_name = 'password_change_done.html'),
        name = 'password_change_done'),
    path('settings/account/', accounts_views.UserUpdateView.as_view(), name='my_account'),

    path('new_post/', views.new_post, name='new_post'),
    path('new_post/', views.NewPostView.as_view(), name='new_post')
]
