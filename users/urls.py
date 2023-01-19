from django.urls import path
from users import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='logout'),
    path('vendor/<int:pk>/', views.vendor_detail, name='vendor_detail'),
    path('my-store/', views.my_store, name='my_store'),
    path('my-store/add-products/', views.add_product, name='add_product'),
    path('my-store/edit-product/<int:pk>/', views.edit_product, name='edit_product'),
    path('my-store/delete-product/<int:pk>/', views.delete_product, name='delete_product'),
    path('myaccount/', views.myaccount, name='myaccount'),
    
]