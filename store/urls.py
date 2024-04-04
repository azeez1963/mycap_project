from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.UpgradedCategoryEndpoint.as_view(), name='category'),
    path('category-list/', views.CategoryListEndpoint.as_view(), name='category-list'),
    path('category/<int:pk>', views.SingleCategoryEndpoint.as_view(), name='category_single'),
    path('category/<int:pk>/delete', views.CategoryDeleteEndpoint.as_view(), name='category-delete'),
    path('product/', views.UpgradedProductEndpoint.as_view(), name='product-details'),
    path('product-list/', views.ProductListEndpoint.as_view(), name='product-list'),
    path('product/<int:product_id>', views.ProductDetailEndpoint.as_view(), name='product_id'),
    path('store/<int:pk>/delete', views.StoreDeleteView.as_view(), name='store-delete'),
    path('store-list/', views.StoreListView.as_view(), name='store-list'),
    path('store-update/', views.StoreUpdateView.as_view(), name='store-update'),
    path('store/', views.StoreCreate.as_view(), name='store-details'),
]
