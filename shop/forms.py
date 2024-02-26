from django import forms

from shop.models import Item

class StyleFormMixin:
    """Form stylization"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class ItemForm(StyleFormMixin, forms.ModelForm):
    """Форма для модели Item"""

    class Meta:
        model = Item
        fields = "__all__"
