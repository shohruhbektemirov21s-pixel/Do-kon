from django.db import models

# Create your models here.
class books:
    def __init__(self, author, year, price):
        self.author = author
        self.year = year
        self.price = price


    def ganir(self, ganir):
        self.ganir = ganir
        return (f"Janr: {self.ganir}")

    def get_info(self):
        return (f"Author: {self.author}, Year: {self.year}, Price: {self.price}")
    
    def set_price(self, new_price):
        self.price = new_price
        return (f"New Price: {self.price}")


books1 = books(author="J.K. Rowling", year=1997, price=20)
print(books1.ganir("Fantasy"))
print(books1.get_info())
print(books1.set_price(25))

class foods:
    def __init__(self, name, calories, price):
        self.name = name
        self.calories = calories
        self.price = price


    def type(self, food_type):
        self.food_type = food_type
        return(f"type: {self.food_type}")

    def get_info(self):
        return(f"Name: {self.name}, Calories: {self.calories}, Price: {self.price}")

    def set_price(self, new_price):
        self.price = new_price
        return(f"New Price: {self.price}")

foods1 = foods(name="Pizza", calories=250, price=15)
print(foods1.type("Fast Food"))
print(foods1.get_info())
print(foods1.set_price(20))


from django.db import models

class mahsulotlar:
    def __init__(self,nomi,narxi,uzunligi):
        self.nomi=nomi
        self.narxi=narxi
        self.uzunligi=uzunligi
    def turi(self,turi):
        self.turi=turi
        return (f"Turi: {self.turi}")
    def get_info(self):
        return (f"Nomi: {self.nomi}, Narxi: {self.narxi}, Uzunligi: {self.uzunligi}")
    def set_price(self,yangi_narxi):
        self.narxi=yangi_narxi
        return (f"Yangi narxi: {self.narxi}")
mahsulot1=mahsulotlar(nomi="Telefon",narxi=1000,uzunligi="15 sm")
print(mahsulot1.turi("Elektronika"))
print(mahsulot1.get_info())
print(mahsulot1.set_price(1200))
 
 from django.db import models

class Mahsulot(models.Model):
    nomi = models.CharField(max_length=100)
    narxi = models.IntegerField()
    uzunligi = models.CharField(max_length=50)

    def __str__(self):
        return self.nomi
