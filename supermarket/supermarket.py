# Create classes to manage a supermarket
class Supermarket:
    """Sample class for a supermarket"""
    
    def __init__(self, name, street,city):
        """Initialize general attributes of every supermarket"""
        self.supermarket_name = str(name).title()
        self.street = str(street).title()
        self.location = str(city).title()
        self.employees = []
        self.products = []

import datetime
class Employee:
    """Sample class for an employee"""
    
    def __init__(self, name, age, pers_id, job):
        """Initialize general attributes of every employee"""
        self.employee_name = str(name).title()
        self.employee_age = int(age)
        self.pers_id = int(pers_id)
        self.job = str(job).title()
        
    def greet_customer(self):
        """Greet a customer politely"""
        current_time = datetime.datetime.now().strftime('%H:%M')
        print(f'Guten Tag. Mein Name ist {self.employee_name} und ich bin {self.job} in diesem Supermarkt. Es ist momentan {current_time} Uhr - wie kann ich Ihnen helfen?')
    
    def celebrate_birthday(self):
        """Celebrate the employee's birthday"""
        print(f'Juhu! Heute werde ich {self.employee_age + 1} Jahre alt!')

class Product:
    """Sample class for all products"""
    
    def __init__(self, name, prod_id, category, price):
        """Initialize general attributes of every product"""
        self.product_name = str(name).title()
        self.prod_id = int(prod_id)
        if category in ["food", "drinks"]:
            self.category = str(category)
        else:
            self.category = "others"
        self.price = float(price)
    
    def test(self):
        print(f'{self.product_name} {self.prod_id} {self.category} {self.price}')
        
    def apply_discount(self, discount):
        if 0 <= float(discount) <= 100:
            self.discount = self.price - ((self.price/100) * float(discount))
        else:
            self.discount = self.price - ((self.price/100) * 5)
        print(f'{self.product_name} {self.prod_id} {self.category} {self.discount}')


