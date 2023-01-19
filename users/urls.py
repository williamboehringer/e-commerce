from django.urls import path
from users import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('vendor/<int:pk>/', views.vendor_detail, name='vendor_detail'),
    path('myaccount/', views.myaccount, name='myaccount'),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='logout'),
]