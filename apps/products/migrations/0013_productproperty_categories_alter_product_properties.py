# Generated by Django 4.1.7 on 2023-03-11 14:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0012_alter_productpropertyvalue_product"),
    ]

    operations = [
        migrations.AddField(
            model_name="productproperty",
            name="categories",
            field=models.ManyToManyField(
                related_name="product_properties",
                to="products.category",
                verbose_name="Категории продуктов",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="properties",
            field=models.ManyToManyField(
                related_name="products",
                through="products.ProductPropertyValue",
                to="products.productproperty",
                verbose_name="Свойства",
            ),
        ),
    ]