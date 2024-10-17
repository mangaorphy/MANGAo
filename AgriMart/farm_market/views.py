from django.shortcuts import render
from django.db.models import Count
from django.views import View
from django.views.generic import ListView, TemplateView
from rest_framework import generics
from .models import Product, Cart, Order, DeliveryCrew
from .serialisers import ProductSerializer, CartSerializer, OrderSerializer, DeliveryCrewSerializer
from .forms import CustomerRegistrationForm

class HomeView(TemplateView):
    template_name = 'farm_market/home.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Query all products (you can filter by category if needed)
        context['products'] = Product.objects.all()
        return context

class AboutView(TemplateView):
    template_name = 'farm_market/about.html'

class ContactView(TemplateView):
    template_name = 'farm_market/contact.html'


class CustomerRegistrationView(TemplateView):
    template_name = 'farm_market/customerregistration.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CustomerRegistrationForm()
        return context

class ProductListView(ListView):
    model = Product
    template_name = 'farm_market/category.html'  
    context_object_name = 'products'

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CartView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class DeliveryCrewListView(generics.ListCreateAPIView):
    queryset = DeliveryCrew.objects.all()
    serializer_class = DeliveryCrewSerializer

class DeliveryCrewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeliveryCrew.objects.all()
    serializer_class = DeliveryCrewSerializer

class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CategoryView(View):
    def get(self,request, val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title').annotate(total= Count('title'))
        return render(request, "farm_market/category.html", locals())

class CategoryTitle(View):
    def get(self,request,val):
        prodcut= Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values("title")
        return render(request, "farm_market/category.html", locals())

class ProductDetail(View):
    def get(self,request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, "farm_market/product_detail.html", locals())

