from django.urls import path
from Connect import views
app_name = 'Connect'
urlpatterns = [
    path('', views.loginUser, name='login'),
    path('register/', views.registerUser, name='register'),
    path('chat/', views.chat, name='chat'),
    path('logout2/', views.logoutUser, name='logout'),
    path('test/', views.testView.as_view, name='test'),
    # path('login', views.CustomLoginView.as_view(), name='login2'),
    # path('logout', views.LogoutView.as_view(), name='logout2'),
    path('login/', views.LoginView.as_view()),
    path('door-click/', views.DoorClickView.as_view()),
    path('users/', views.UserListView.as_view()),
    path('users/<int:user_id>/clicks/', views.UserClicksView.as_view()),
    path('users/create/', views.CreateUserView.as_view()),
]