from django.urls import path
from Connect import views
app_name = 'Connect'
urlpatterns = [
    path('', views.loginUser, name='login'),
    path('register/', views.registerUser, name='register'),
    path('chat/', views.chat, name='chat'),
    path('logout/', views.logoutUser, name='logout'),
    path('test/', views.testView.as_view, name='test'),
]