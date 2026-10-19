from django import forms
from catalog.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # Поля вашей модели для заполнения пользователем
        fields = ['name', 'description', 'image', 'category', 'price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Добавляем стили к полям, чтобы форма выглядела красиво
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'style': 'width: 100%; padding: 10px; margin-bottom: 15px; border: 1px solid #dee2e6; border-radius: 6px; box-sizing: border-box; font-size: 1rem;'
            })
