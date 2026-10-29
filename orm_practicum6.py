from datetime import timedelta
from random import randint, choice

from django.utils import timezone
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from store.models import *

# Задача 1
# Цель: Вычислить общую стоимость всех продуктов в базе данных.
# Инструкция:
# 1. Используйте модель Product.
# 2. Рассчитайте общую стоимость всех продуктов (цена умноженная на количество) в базе данных.

from django.db.models import Sum, F, Avg, Min, Max
from store.models import Product, Category

# total_value = Product.objects.aggregate(total_value=Sum(F('price')*F('quantity')))['total_value']
# print(total_value)


# Задача 2
# Цель: Вычислить среднюю цену продуктов для каждой категории.
# Инструкция:
# 1. Используйте модели Product и Category.
#2. Группируйте продукты по категориям и вычислите среднюю цену для каждой категории.

# avg_price_category = Product.objects.values('category__name').annotate(avg_price=Avg('price')).order_by('category__name')
#
# for category in avg_price_category:
#     print({category['category__name']}, category['avg_price'])
#
#
# average_price_by_category = Product.objects.values('category__id', 'category__name').annotate(
#     average_price=Avg('price')).order_by('category__name')
#
# for entry in average_price_by_category:
#     print(f"Категория: {entry['category__name']}, Средняя цена: {entry['average_price']:.2f}")

# Задача 3
# Цель: Найти самый дешевый и самый дорогой продукт.
# Инструкция:
# 1. Используйте модель Product.
# 2. Найдите продукт с минимальной ценой и продукт с максимальной ценой.

from django.db.models import Min, Max, Count, F, ExpressionWrapper, fields
from store.models import Product, Customer, Order, OrderItem, ProductDetail

cheapest_product = Product.objects.aggregate(min_price=Min('price'))['min_price']
most_expensive_product = Product.objects.aggregate(max_price=Max('price'))['max_price']

print(f"Самый дешевый продукт: {cheapest_product}")
print(f"Самый дорогой продукт: {most_expensive_product}:")

# Задача 4
# Цель: Вычислить количество заказов и общую стоимость заказов для каждого клиента.
# Инструкция:
# 1. Используйте модели Order, OrderItem, и Customer.
# 2. Группируйте по клиентам и вычислите количество заказов и общую стоимость заказов для каждого клиента.
# orders_summary_by_customer = (
#     Order.objects
#     .values('customer__first_name', 'customer__last_name')
#     .annotate(
#         order_count=Count('id', distinct=True),
#         total_spent=Sum(F('items__price') * F('items__quantity'))
#     )
#     .order_by('customer__last_name')
# )
#
# for entry in orders_summary_by_customer:
#     print(
#         f"Клиент: {entry['customer__first_name']} {entry['customer__last_name']}, "
#         f"Заказов: {entry['order_count']}, "
#         f"Общая сумма: {entry['total_spent']}"
#     )

# Задача 5
# Цель: Рассчитать общий вес всех продуктов для каждой категории.
# Инструкция:
# 1. Используйте модели Product, ProductDetail, и Category.
# 2. Группируйте по категориям и вычислите общий вес всех продуктов в каждой категории.

# total_weight_by_category = Product.objects.values('category__name').annotate(
#     total_weight=Sum(F('detail__weight') * F('quantity'))
# ).order_by('category__name')
#
# for entry in total_weight_by_category:
#     print(f"Категория: {entry['category__name']}, Общий вес: {entry['total_weight']}")


# Задача 6
# Цель: Вычислить количество различных продуктов, которые поставляет каждый поставщик.
# Инструкция:
# 1. Используйте модели Product и Supplier.
# 2. Группируйте продукты по поставщикам и подсчитайте количество продуктов для каждого поставщика.

# products_count_by_supplier = Product.objects.values('supplier__name').annotate(
#     count=Count('id')
# ).order_by('supplier__name')
#
# for entry in products_count_by_supplier:
#     print(f"Поставщик: {entry['supplier__name']}, Количество продуктов: {entry['count']}")

# Задача 7
# Цель: Вычислить среднюю продолжительность жизни продуктов (в днях) на основе даты производства и
# срока годности.
# Инструкция:
# 1. Используйте модели Product и ProductDetail.
# 2. Рассчитайте среднее время от даты производства до срока годности для всех продуктов.
# from django.db.models import Avg, F, ExpressionWrapper, DurationField
# from store.models import Product, ProductDetail
#
# average_lifespan = (
#     ProductDetail.objects
#     .annotate(lifespan=ExpressionWrapper(F('expiration_date') - F('manufacturing_date'), output_field=DurationField()))
#     .aggregate(average_lifespan=Avg('lifespan'))
# )['average_lifespan']
#
# if average_lifespan is not None:
#     average_lifespan_days = average_lifespan.total_seconds() / (24 * 3600)
#     print(f"Средняя продолжительность жизни продуктов: {average_lifespan_days:.2f} дней")
# else:
#     print("Нет данных для расчета средней продолжительности жизни продуктов.")

# Задача 8
# # Цель: Рассчитать общую сумму всех заказов для каждого клиента.
# # Инструкция:
# # 1. Используйте модели OrderItem, Order, и Customer.
# # 2. Группируйте заказы по клиентам и вычислите общую сумму заказов для каждого клиента.

# from django.db.models import Sum, F
# from store.models import Order, Customer, OrderItem
#
# total_spending_by_customer = (
#     Order.objects
#     .values('customer__first_name', 'customer__last_name')
#     .annotate(total_spent=Sum(F('items__price') * F('items__quantity')))
#     .order_by('customer__last_name')
# )
# for entry in total_spending_by_customer:
#     print(
#         f"Клиент: {entry['customer__first_name']} {entry['customer__last_name']}, "
#         f"Общая сумма заказов: {entry['total_spent']:.2f}"
#     )


"""Order_by"""

# Задача 1
# Цель: Сортировать список продуктов по их цене в порядке убывания.
# Инструкция:
# 1. Используйте модель Product.
# 2. Получите список продуктов, отсортированных по цене в порядке убывания.

product_desc = Product.objects.all().order_by('-price')

for product in product_desc:
    print(f"Продукт: {product.name}, Цена: {product.price}")

# Задача 2
# Цель: Сортировать список заказов по их общей стоимости.
# Инструкция:
# 1. Используйте модели Order и OrderItem.
# 2. Получите список заказов, отсортированных по их общей стоимости в порядке убывания.

# from django.db.models import Sum, F
# from store.models import Order
# # Сортировка заказов по общей стоимости
#
# orders_sorted_by_total = Order.objects.annotate(
#     total_cost=Sum(F('items__price') * F('items__quantity'))
# ).order_by('-total_cost')
#
# print("Заказы, отсортированные по общей стоимости:")
# for order in orders_sorted_by_total:
#     print(f"Заказ №{order.pk}, Общая стоимость: {order.total_cost:.2f}")


# Задача 3
# Цель: Отсортировать список адресов сначала по стране, затем по городу.
# Инструкция:
# 1. Используйте модель Address.
# 2. Получите список адресов, отсортированных по стране и затем по городу в алфавитном порядке.

# from store.models import Address
#
# addresses_sorted = Address.objects.order_by('country', 'city')
# for address in addresses_sorted:
#     print(f"Адрес: {address.street}, Город: {address.city}, Страна: {address.country}")

# Задача 4
# Цель: Отсортировать список заказов по количеству позиций в каждом заказе.
# Инструкция:
# 1. Используйте модели Order и OrderItem.
# 2. Получите список заказов, отсортированных по количеству позиций в каждом заказе
# from django.db.models import Count
# from store.models import Order
# # Сортировка заказов по количеству позиций заказа
#
# orders_sorted_by_item_count = Order.objects.annotate(
#     item_count=Count('items')).order_by('-item_count')
#
# for order in orders_sorted_by_item_count:
#     print(f"Заказ №{order.pk}, Количество позиций: {order.item_count}")


# Задача
# Цель: Найти все заказы, сделанные за последний месяц.
# Инструкция:
# 1. Используйте модель Order.
# 2. Используйте фильтр для поиска заказов, сделанных в последний месяц от текущей даты.
# from django.utils import timezone
# from store.models import Order
#
# last_month = timezone.now() - timedelta(days=30)
# recent_orders = Order.objects.filter(order_date__gte=last_month)
# print("Заказы за последний месяц:")
# for order in recent_orders:
#     print(f"Заказ {order.id}, Дата: {order.order_date}")


#Срезы
# Задача 1
# Цель: Извлечь первые 5 продуктов из списка всех продуктов.
# Инструкция:
# 1. Используйте модель Product.
# 2. Используйте срез для получения первых 5 продуктов.
from store.models import Product
# Первые 5 продуктов
first_five_products = Product.objects.all()[:5]
print("Первые 5 продуктов:")
for product in first_five_products:
    print(f"{product.name}: {product.price}")

# Задача 2
# Цель: Найти 10 самых дорогих продуктов.
# Инструкция:
# 1. Используйте модель Product.
# 2. Используйте order_by для сортировки продуктов по цене в порядке убывания.
# 3. Используйте срез для получения первых 10 записей.

from store.models import Product
# 10 самых дорогих продуктов
top_ten_expensive_products = Product.objects.order_by('-price')[:10]
print("10 самых дорогих продуктов:")
for product in top_ten_expensive_products:
    print(f"{product.name}: {product.price}")

