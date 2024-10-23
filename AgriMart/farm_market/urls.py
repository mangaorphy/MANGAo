from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm

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
    CustomerRegistrationView,
    profile_view,
    address,
    UpdateProfileView,
    UpdateAddressView
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
    path('login/',auth_view.LoginView.as_view(template_name='farm_market/Login.html', authentication_form=LoginForm), name='login'),
    path('password_reset/', auth_view.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_view.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_view.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('profile/', profile_view, name='profile'),
    path('address/', address, name='address'),
    path('profile/update/', UpdateProfileView.as_view(), name='update_profile'),
    path('profile/address/update/', UpdateAddressView.as_view(), name='update_address'),
    path('password_change/', auth_view.PasswordChangeView.as_view(template_name='farm_market/password_change_form.html'), name='password_change'),
    path('password_change_done/', auth_view.PasswordChangeDoneView.as_view(template_name='farm_market/password_change_done.html'), name='password_change_done'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)