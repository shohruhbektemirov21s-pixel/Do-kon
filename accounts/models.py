from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    size = models.CharField(max_length=50, blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.price} so'm"

    def set_price(self, new_price):
        self.price = new_price
        self.save()
        return self.price

    def get_info(self):
        return f"Mahsulot: {self.name}, Narxi: {self.price}, Uzunligi: {self.size}, Kategoriya: {self.category}"
