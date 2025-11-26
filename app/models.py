from django.db import models
from decimal import Decimal


class Datebase(models.Model):
    created_ad = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    update_ad = models.DateTimeField(auto_now =True,null=True,blank=True)

    class Meta:
        abstract = True



class Category(Datebase):
    title = models.CharField(max_length=255,null=True, blank=True) 

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'categories'





class Product(Datebase):
    name = models.CharField(max_length=255,null = True,  blank= True)
    price = models.DecimalField(max_digits=14,decimal_places=2)
    description = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='products/',null=True,blank=True)
    stock = models.PositiveSmallIntegerField(default=1)
    discount = models.PositiveSmallIntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,related_name='products',null=True,blank=True)    
    
    def __str__(self):
        return self.name

    @property
    def discount_price(self):
        if self.discount:
            return self.price * Decimal(f"{1 - self.discount / 100}")
        return self.price
    


    
class Order(Datebase):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.product.name}"
    





class Comment(Datebase):
    class RatingChoices(models.IntegerChoices):
        ONE = 1, "⭐ 1"
        TWO = 2, "⭐⭐ 2"
        THREE = 3, "⭐⭐⭐ 3"
        FOUR = 4, "⭐⭐⭐⭐ 4"
        FIVE = 5, "⭐⭐⭐⭐⭐ 5"
    
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField(null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='comments')
    image = models.ImageField(upload_to='comments/%Y/%m/%d/',null=True,blank=True)
    rating = models.PositiveSmallIntegerField(choices=RatingChoices.choices,default = RatingChoices.FIVE)
    is_handle = models.BooleanField(default=False)
    
    


    def __str__(self):
        return f'{self.name} - {self.message}'


