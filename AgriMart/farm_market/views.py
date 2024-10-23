from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.views import View
from django.views.generic import ListView, TemplateView
from rest_framework import generics
from .models import Product, Cart, Order, DeliveryCrew
from .serialisers import ProductSerializer, CartSerializer, OrderSerializer, DeliveryCrewSerializer
from .forms import CustomerRegistrationForm, ProfileForm, AddressForm
from django.contrib import messages
from django.urls import reverse_lazy

from .forms import ProfileForm

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

    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulations! User register Successfully")
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request,'farm_market/customerregistration.html',locals())

class CustomLoginView(LoginView):
    template_name = 'farm_market/login.html'

    def form_valid(self, form):
        messages.success(self.request, "You have successfully logged in!")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('profile')  # Redirect to profile page after login

@login_required
def profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the same home page
    else:
        form = ProfileForm(instance=request.user.profile)
    
    return render(request, 'farm_market/profile.html', {'form': form})

def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'farm_market/address.html', locals())

# Profile Update View
class UpdateProfileView(View):
    def get(self, request):
        form = ProfileForm(instance=request.user.profile)
        return render(request, 'farm_market/profile.html', {'form': form})

    def post(self, request):
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home after successful update
        return render(request, 'farm_market/profile.html', {'form': form})

# Address Update View
class UpdateAddressView(View):
    def get(self, request):
        form = AddressForm(instance=request.user.profile)  # Assuming address fields are part of the profile
        return render(request, 'farm_market/updateAddress.html', {'form': form})

    def post(self, request):
        form = AddressForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home after updating the address
        return render(request, 'farm_market/updateAddress.html', {'form': form})


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

