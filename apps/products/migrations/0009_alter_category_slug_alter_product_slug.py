# Generated by Django 4.1.7 on 2023-03-08 19:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0008_category_remove_productproperty_order_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="slug",
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
