class Children:
    def __init__(self):
        self.sum = 0
    
    def take_food(self, price):
        self.sum += price
    
    def take_sortdrink(self, price):
        self.sum += price
    
    def take_alhocol(self, price=500):
        pass
    
    def get_sum(self):
        return self.sum

class Adult(Children):
    def __init__(self):
        super().__init__()
        self.alcohol = False
        
    def take_food(self, price):
        if self.alcohol:
            self.sum += price - 200
    
    def take_alhocol(self, price=500):
        self.sum += price
        self.alcohol = True

n, k =  map(int, input().split())

customers = [None] * n
for i in range(n):
    age = int(input())
    if age >= 20:
        customers[i] = Adult()
    else:
        customers[i] = Children()
    
for _ in range(k):
    values = list(input().split())
    index = int(values[0]) - 1
    order = values[1]
    
    if order == "0":
        customers[index].take_alhocol()
    else:
        price = int(values[2])
        
        if order == "food":
            customers[index].take_food(price)
        elif order == "softdrink":
            customers[index].take_sortdrink(price)
        elif order == "alcohol":
            customers[index].take_alhocol(price)
            
for i in customers:
    print(i.get_sum())
            