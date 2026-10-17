from django.urls import path
# Добавляем в импорт контроллеры, включая новый product_detail_view
from catalog.views import (
    home_view, categories_view, orders_view, contacts_view, product_detail_view, create_product_view
)

# исключаем одноименные конфликты
app_name = 'catalog'

urlpatterns = [
    # маршрут для домашней страницы 1
    path('', home_view, name='21-2_home1'),

    # маршрут для Категорий страница 2
    path('categories/', categories_view, name='21-2_home2'),

    # маршрут для Заказов страница 3
    path('orders/', orders_view, name='21-2_home3'),

    # маршрут для страницы 4 контактов с закрывающим /
    path('contacts/', contacts_view, name='21-2_home4'),

    # НОВЫЙ МАРШРУТ ПО ТЗ (Задание 1)
    path('products/<int:pk>/', product_detail_view, name='product_detail'),

    path('products/create/', create_product_view, name='create_product'),
]

#----------23--

# from django.urls import path
# # Добавляем в импорт контроллеры
# from catalog.views import home_view, categories_view, orders_view, contacts_view
#
#
# # исключаем одноименные конфликты
# app_name = 'catalog'
#
#
# urlpatterns = [
#     # маршрут для домашней страницы 1
#     path('', home_view, name='21-2_home1'),
#
#     # маршрут для Категорий страница 2
#     path('categories/', categories_view, name='21-2_home2'),
#
#     # маршрут для Заказов страница 3
#     path('orders/', orders_view, name='21-2_home3'),
#
#     # маршрут для страницы 4 контактов с закрывающим /
#     path('contacts/', contacts_view, name='21-2_home4'),
# ]
