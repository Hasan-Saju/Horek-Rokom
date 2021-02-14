from django.urls import path
from App_Shop import views

app_name = 'App_Shop'


urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('product_details/<pk>/',views.ProductDetail.as_view(),name='product_details'),
    path('category/',views.View_Category,name='category'),
    path('categoryWise/<pk>/',views.ProductDetail_from_Category,name='categoryWise'),
]
