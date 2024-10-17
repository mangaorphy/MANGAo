from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    ProductListView,
    ProductDetailView,
    CartView,
    OrderCreateView,
    OrderDetailView,
    DeliveryCrewDetailView,
    DeliveryCrewListView,
    #home,
    ProductListAPIView,
    AboutView,
    ContactView,
    HomeView,
    CategoryView,
    ProductDetail,
    CategoryTitle,
    CustomerRegistrationView
)

urlpatterns = [
    path('products/', ProductListView.as_view(), name='products'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('home/', HomeView.as_view(), name='home'),
    path('api/products/', ProductListAPIView.as_view(), name='api-product-list'),  # API view
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('orders/', OrderCreateView.as_view(), name='order-create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('delivery-crew/', DeliveryCrewListView.as_view(), name='delivery-crew-list'),
    path('delivery-crew/<int:pk>/', DeliveryCrewDetailView.as_view(), name='delivery-crew-detail'),
    #path('home/', home, name="home"),
    path('category/<slug:val>', CategoryView.as_view(), name='category'),
    path('category-title/<val>', CategoryTitle.as_view(), name='category-title'),
    path('product_detail/<int:pk>', ProductDetail.as_view(), name='product_detail'),

    #login authentication
    path('registration/', CustomerRegistrationView.as_view(),name='customerregistration' ),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)