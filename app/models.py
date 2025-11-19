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
    



class User(models.Model):
    first_name = models.CharField(max_length=255,null=True,blank=True)
    last_name = models.CharField(max_length=255,null=True,blank=True)
    phone = models.CharField(max_length=20, unique=True, null=True, blank=True)
    email = models.EmailField(null=True,blank=True)


    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    



class Comment(Datebase):
    user = models.ForeignKey(User, on_delete=models.CASCADE)   
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    text = models.TextField(null=True,blank=True)                                      
    rating = models.IntegerField(default=5)
      

    def __str__(self):
        return f"{self.user.full_name} - {self.product.name}"



