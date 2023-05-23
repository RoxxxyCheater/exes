from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.TextField(max_length=600)
    img_url=models.TextField(max_length=600) 
    prod_url=models.TextField(max_length=600)
 
    # class Meta:
    #     app_label = 'product'
        
    def __str__(self):
        return '%s %s %s' % (self.title,self.img_url, self.prod_url)