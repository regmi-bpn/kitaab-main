from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
    path('', views.index, name='ShopHome'),
    path('about/', views.about, name='AboutUs'),
    path('contact/', views.contact, name='ContactUs'),
    path('tracker/', views.tracker, name='TrackingStatus'),
    path('search/', views.search, name='Search'),
    path('products/<int:myid>', views.productview, name='ProductView'),
    path('checkout/', views.checkout, name='Checkout'),
]

admin.site.site_header = "Kitaab Admin"
admin.site.site_title = "Kitaab Admin Portal"
admin.site.index_title = "Welcome to Kitaab Admin Portal"