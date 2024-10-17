from django.db import models

class Farmer(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=255)

    def __str__(self):
        return self.name

CATEGORY_CHOICES =(
    ('CR','Cereals'),
    ('VEG', 'Vegetables'),
    ('FRUT', 'Fruits'),
    ('LEG', 'Legumes'),
    ('DEF', 'Any product'),
)

class Product(models.Model):
    farmer = models.ForeignKey(Farmer, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    selling_price = models.FloatField(default=0.0)
    discounted_price = models.FloatField(default=0.0)
    composition = models.TextField(default="")
    prodapp = models.TextField(default="")
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=5, default='DEF')
    product_image = models.ImageField(upload_to="product", null=True, blank=True)

    def __str__(self):
        return self.title

class Cart(models.Model):
    user = models.CharField(max_length=100)  # Can be linked to a user model later
    products = models.ManyToManyField(Product, through='CartItem')

    def __str__(self):
        return f"Cart of {self.user}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

class DeliveryCrew(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=255)
    assigned_orders = models.ManyToManyField('Order', related_name='delivery_crews', blank=True)  # Updated related_name

    def __str__(self):
        return self.name

class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    buyer_name = models.CharField(max_length=100)
    delivery_address = models.CharField(max_length=255)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ])
    delivery_crew = models.ForeignKey(DeliveryCrew, related_name='orders', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Order by {self.buyer_name} on {self.order_date}"