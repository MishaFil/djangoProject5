from django.contrib import admin
from django.urls import path
from main.models import Category, Product
from main.views import my_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', my_view, name='my_view'),
]


def load_data():
    categories_data = """1:Велосипеды:None
                        2:Кастрюли:4
                        3:Тарелки:4
                        4:Посуда для кухни:5
                        5:Товары для дома:None"""

    products_data = """1:Велосипед:1:100:100.50
                       2:Кастрюля 1,5л:2:50:1200
                       3:Тарелка 25см:3:1000:25
                       4:Кастрюля 3л:55:300.78"""

    for category_row in categories_data.split('\n'):
        category_info = category_row.split(':')
        category = Category(id=int(category_info[0]), title=category_info[1],
                            parent_id=category_info[2] if category_info[2] != 'None' else None)
        category.save()

    for product_row in products_data.split('\n'):
        product_info = product_row.split(':')
        product = Product(id=int(product_info[0]), title=product_info[1], category_id=int(product_info[2]),
                          count=int(product_info[3]), cost=float(product_info[4]))
        product.save()
