from django.shortcuts import render, get_object_or_404, redirect
from catalog.models import Product, ContactInfo
from catalog.forms import ProductForm


def home_view(request):
    """Контроллер главной страницы"""
    # -24- используем лаконичный запрос для всех товаров
    products_all = Product.objects.all()

    # Вывод в консоль для проверки (выведет первые 5 из всех)
    print("\n--- ПОСЛЕДНИЕ ПРОДУКТЫ В КОНСОЛИ ---")
    for product in products_all[:5]:
      print(f"ID: {product.id} | {product.name} | Цена: {product.price} руб.")
    print("---------------------------------------\n")

    # Передаем все товары в шаблон
    return render(request, 'catalog/home.html', {'products': products_all})


def categories_view(request):
    """Контроллер для страницы категорий"""
    # Забираем все продукты, чтобы вывести их на странице категорий
    products_all = Product.objects.all()
    # Передаем их в шаблон под ключом 'products'
    return render(request, 'catalog/21-2_home2.html', {'products': products_all})


def orders_view(request):
    """Контроллер для страницы заказов"""
    return render(request, 'catalog/21-2_home3.html')


def contacts_view(request):
    """Контроллер страницы контактов"""
    context = {}

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        print(f"Новое сообщение!")
        print(f"Имя: {name} | Email: {email}")
        print(f"Текст: {message}")
        print("-" * 20)

        context['success_message'] = 'Спасибо! Ваше сообщение успешно отправлено.'

    try:
      context['contact_data'] = ContactInfo.objects.first()
    except Exception:
      context['contact_data'] = None

    return render(request, 'catalog/contacts.html', context)


# -24-(Задание 1)
def product_detail_view(request, pk):
    """Контроллер страницы с подробной информацией о товаре"""
    # Получаем pk из URL, извлекаем объект через ORM или отдаем 404
    product = get_object_or_404(Product, pk=pk)
    # Передаем объект в шаблон детальной страницы
    return render(request, 'catalog/product_detail.html', {'product': product})


# -24-(Дополнительное задание 1)
def create_product_view(request):
    """Контроллер формы для создания нового товара с защитой и валидацией"""
    if request.method == 'POST':
        # Если пользователь нажал кнопку "Сохранить", передаем данные в форму
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Форма валидна — сохраняем новый товар в БД
            return redirect('catalog:21-2_home1')  # Перенаправляем на главную
    else:
        # Если пользователь просто открыл страницу — отдаем пустую форму
        form = ProductForm()

    return render(request, 'catalog/product_form.html', {'form': form})
