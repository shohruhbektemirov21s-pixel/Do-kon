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