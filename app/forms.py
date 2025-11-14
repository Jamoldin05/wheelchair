from django import forms
from .models import Product, Order, Comment


class ProductFormsModel(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ()


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ()

    def clean(self):
        cleaned_data = super().clean()
        product = cleaned_data.get('product')
        quantity = cleaned_data.get('quantity')

        if product and quantity:
            if quantity > product.stock:
                raise forms.ValidationError(f"Available stock is {product.stock}. You cannot order {quantity}.")




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ()