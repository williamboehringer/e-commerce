from django.urls import path
from users import views

urlpatterns = [
    path('vendor/<int:pk>/', views.vendor_detail, name='vendor_detail'),
    path('myaccount/', views.myaccount, name='myaccount'),
    path('signup/', views.signup, name='signup'),
]