# Generated by Django 4.1.7 on 2023-03-08 19:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0007_alter_productpropertyvalue_value"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("path", models.CharField(max_length=255, unique=True)),
                ("depth", models.PositiveIntegerField()),
                ("numchild", models.PositiveIntegerField(default=0)),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("updated_date", models.DateTimeField(auto_now=True)),
                (
                    "is_published",
                    models.BooleanField(default=False, verbose_name="Опубликовано"),
                ),
                (
                    "ordering",
                    models.PositiveSmallIntegerField(
                        default=500, verbose_name="Порядок"
                    ),
                ),
                ("slug", models.SlugField(blank=True, max_length=100)),
                (
                    "seo_title",
                    models.CharField(
                        blank=True, max_length=250, verbose_name="SEO Title"
                    ),
                ),
                (
                    "seo_description",
                    models.CharField(
                        blank=True, max_length=300, verbose_name="SEO Description"
                    ),
                ),
                ("h1", models.CharField(blank=True, max_length=250, verbose_name="H1")),
                (
                    "is_index",
                    models.BooleanField(default=True, verbose_name="Robots index"),
                ),
                (
                    "is_follow",
                    models.BooleanField(default=True, verbose_name="Robots follow"),
                ),
                (
                    "name",
                    models.CharField(max_length=500, verbose_name="Название продукта"),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, max_length=1500, verbose_name="Описание"
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.RemoveField(
            model_name="productproperty",
            name="order",
        ),
        migrations.AddField(
            model_name="product",
            name="created_date",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product",
            name="h1",
            field=models.CharField(blank=True, max_length=250, verbose_name="H1"),
        ),
        migrations.AddField(
            model_name="product",
            name="is_follow",
            field=models.BooleanField(default=True, verbose_name="Robots follow"),
        ),
        migrations.AddField(
            model_name="product",
            name="is_index",
            field=models.BooleanField(default=True, verbose_name="Robots index"),
        ),
        migrations.AddField(
            model_name="product",
            name="is_published",
            field=models.BooleanField(default=False, verbose_name="Опубликовано"),
        ),
        migrations.AddField(
            model_name="product",
            name="ordering",
            field=models.PositiveSmallIntegerField(default=500, verbose_name="Порядок"),
        ),
        migrations.AddField(
            model_name="product",
            name="seo_description",
            field=models.CharField(
                blank=True, max_length=300, verbose_name="SEO Description"
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="seo_title",
            field=models.CharField(
                blank=True, max_length=250, verbose_name="SEO Title"
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="slug",
            field=models.SlugField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="product",
            name="updated_date",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="productproperty",
            name="created_date",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="productproperty",
            name="is_published",
            field=models.BooleanField(default=False, verbose_name="Опубликовано"),
        ),
        migrations.AddField(
            model_name="productproperty",
            name="ordering",
            field=models.PositiveSmallIntegerField(default=500, verbose_name="Порядок"),
        ),
        migrations.AddField(
            model_name="productproperty",
            name="updated_date",
            field=models.DateTimeField(auto_now=True),
        ),
    ]