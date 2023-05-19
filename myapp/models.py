from django.db import models

# Create your models here.
class product_mst(models.Model):
    product_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.product_name
    
class product_sub_cat(models.Model):
    p_name = models.ForeignKey(product_mst ,on_delete=models.CASCADE)
    product_model = models.CharField(max_length=10)
    product_ram = models.IntegerField()
    product_image = models.FileField(upload_to="product-images", default="default-product-image.jpg")
    product_price = models.IntegerField()

    def __str__(self):
        return f"{self.p_name}, {self.product_model}, {self.product_ram}, {self.product_price}"