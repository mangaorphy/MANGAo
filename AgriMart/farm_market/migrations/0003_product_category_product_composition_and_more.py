# Generated by Django 5.1.2 on 2024-10-14 10:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("farm_market", "0002_deliverycrew_order_delivery_crew"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.CharField(
                choices=[
                    ("CR", "Cereals"),
                    ("VEG", "Vegetables"),
                    ("FRUT", "Fruits"),
                    ("LEG", "Legumes"),
                    ("DEF", "Any product"),
                ],
                default="DEF",
                max_length=5,
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="composition",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="product",
            name="discounted_price",
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name="product",
            name="prodapp",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="product",
            name="product_image",
            field=models.ImageField(blank=True, null=True, upload_to="product"),
        ),
        migrations.AddField(
            model_name="product",
            name="selling_price",
            field=models.FloatField(default=0.0),
        ),
    ]