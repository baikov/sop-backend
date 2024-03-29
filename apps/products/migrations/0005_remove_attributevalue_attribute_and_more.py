# Generated by Django 4.1.7 on 2023-03-08 17:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0004_productproperty_alter_attribute_options_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="attributevalue",
            name="attribute",
        ),
        migrations.RemoveField(
            model_name="product",
            name="properties",
        ),
        migrations.AddField(
            model_name="productproperty",
            name="slug",
            field=models.CharField(
                blank=True, max_length=50, verbose_name="Код свойства"
            ),
        ),
        migrations.DeleteModel(
            name="Attribute",
        ),
        migrations.DeleteModel(
            name="AttributeValue",
        ),
    ]
