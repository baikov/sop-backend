# Generated by Django 4.1.7 on 2023-03-11 20:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0014_remove_product_price_category_price_coefficient_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="price_coefficient",
            field=models.DecimalField(
                decimal_places=2,
                default=1.0,
                max_digits=20,
                verbose_name="Коэфициент цены",
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="weight_coefficient",
            field=models.DecimalField(
                decimal_places=2,
                default=1.0,
                max_digits=20,
                verbose_name="Коэфициент веса",
            ),
        ),
    ]
