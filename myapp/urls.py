from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('menu/', views.menu_page, name="menu"),
    path('order/<int:id>/', views.order_product, name='order_product'),
    path('order_success/<int:order_id>/', views.order_success, name='order_success'),
    path('order_track/', views.Ordertrack, name="track"),
    path('reservation/', views.reservations, name="reservation"),
    path('contact/', views.contact, name="contact"),
    path('search/', views.search, name='search'),
]
