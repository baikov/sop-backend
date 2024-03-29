# Generated by Django 4.1.7 on 2023-03-17 21:41

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0016_remove_product_meter_weight_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="productproperty",
            name="units",
            field=models.CharField(
                blank=True, max_length=250, verbose_name="Единицы измерения"
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=django_extensions.db.fields.AutoSlugField(
                blank=True, editable=False, populate_from="name", verbose_name="slug"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="slug",
            field=django_extensions.db.fields.AutoSlugField(
                blank=True, editable=False, populate_from="name", verbose_name="slug"
            ),
        ),
    ]
