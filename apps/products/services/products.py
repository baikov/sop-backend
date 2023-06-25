from django.db.models import Subquery
from django.db.models.query import QuerySet

from apps.products.filters import ProductFilter
from apps.products.models import Product


def get_products_list(filters: dict = None) -> QuerySet:
    """
    Возвращает список объектов. Реализована фильтрация.
    """
    filters = filters or {}
    qs = Product.objects.filter(is_published=True)
    return ProductFilter(filters, qs).qs


def add_product_properties(product: Product) -> None:
    """
    Создает записи таблицы ProductPropertyValue (Свойство - Значение) для вновь
    созданного Продукта на основе принадлежности к Категории
    """
    category = product.categories.filter(product_categories__is_primary=True).first()
    if category is None:
        return
    properties = category.product_properties.difference(product.properties.all())
    for property in properties:
        product.properties_through.create(property=property)


def remove_redundant_product_properties(product: Product) -> None:
    """
    Удаляет записи таблицы ProductPropertyValue (Свойство - Значение) для Продукта
    при смене Категории
    """
    # TODO: проверить на корректность работы
    category = product.categories.filter(product_categories__is_primary=True).first()
    remove_properties = product.properties.difference(category.product_properties.all())
    product.properties_through.filter(
        property_id__in=Subquery(remove_properties.values("id"))
    ).delete()
    # product.properties_through.filter(property__in=remove_properties).delete()
