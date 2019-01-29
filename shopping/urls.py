from django.urls import path
from .views import ( 
    ProductListView, 
    ProductDetailView,
    ProductCreateView 
    )
from . import views

urlpatterns = [
    path('', ProductListView.as_view(), name="shopping-home"),
    path('search/', views.search, name='search'),
    path('book/<int:pk>/', ProductDetailView.as_view(), name="product-detail"),
    path('book/new', ProductCreateView.as_view(), name="product-create"),
]