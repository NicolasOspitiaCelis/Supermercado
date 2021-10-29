from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView)
from supermercadoApp import views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', views.UserCreateView.as_view()),
    path('users/', views.UserListView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),
    path("user-update/<int:pk>/", views.UserUpdateView.as_view()),
    path('user-delete/<int:pk>/', views.UserDeleteView.as_view()),
    path('producto/', views.ProductoCreateView.as_view()),
    path('productos/', views.ProductoListView.as_view()),
    path('producto/<int:pk>/', views.ProductoDetailView.as_view()),
    path("producto-update/<int:pk>/", views.ProductoUpdateView.as_view()),
    path('producto-delete/<int:pk>/', views.ProductoDeleteView.as_view()),
    path('inventario/', views.InventarioCreateView.as_view()),
    path('inventarios/', views.InventarioListView.as_view()),
    path('inventario/<int:pk>/', views.InventarioDetailView.as_view()),
    path("inventario-update/<int:pk>/", views.InventarioUpdateView.as_view()),
    path('inventario-delete/<int:pk>/', views.InventarioDeleteView.as_view()),
    path('proveedor/', views.ProveedorCreateView.as_view()),
    path('proveedor/<int:pk>/', views.ProveedorDetailView.as_view()),
    path("proveedor-update/<int:pk>/", views.ProveedorUpdateView.as_view()),
    path('proveedores/', views.ProveedorListView.as_view()),
    path('proveedor-delete/<int:pk>/', views.ProveedorDeleteView.as_view()),
    path('compra/', views.CompraCreateView.as_view()),
]
