class Jets:
    model = None
    country = 0
    def __init__(self, name, country, cantidad):
        self.name = name
        self.origin = country
        self.quantity = cantidad
#Escriba su respuesta aquí.        
first_item=Jets("F14","",87)
second_item=Jets("F14","",35)
total= first_item.quantity + second_item.quantity
print(total)