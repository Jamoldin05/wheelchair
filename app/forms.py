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





class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ()