class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def __str__(self):
        return f'{self.name} {self.price}'
    def __eq__(self,other):
        return self.name == other.name
    def __lt__(self,other):
        return self.price < other.price
    def __bool__(self):
        return self.price > 0
    def __len__(self):
        return len(self.name)
    def __add__(self,other):
        new = self.price + other.price
        new2 = self.name +other.name
        return new,new2
    
p1 = Product('socks22',30)
p2 = Product('socks',100)
products = [p1,p2]
for i in sorted(products):
    print(i)
if p1:
    print('Карта ж')
