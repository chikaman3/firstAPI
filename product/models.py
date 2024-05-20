from django.db import models

# Create your models here.

class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True


class Category(TimeStamp):
    category_name = models.CharField(max_length=180)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.category_name
    



class Product(TimeStamp):
      product_name = models.CharField(max_length=180)
      description = models.TextField(max_length=250)
      price = models.DecimalField(max_digits=10 , decimal_places=2)
      image = models.FileField(upload_to='products/')
      Category = models.ForeignKey(Category, on_delete= models.CASCADE)

      def __str__(self):
        return self.product_name

    


class Order(TimeStamp):
     customer_name = models.CharField(max_length=180)
     email = models.EmailField()
     quantity= models.PositiveSmallIntegerField()
     product  = models.ForeignKey(Product, on_delete= models.CASCADE)

     def __str__(self):
        return  f'Order #{self.id}'

    