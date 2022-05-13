class Nobel:

    def __init__(self, tipo, ano, name):
        self.winner = name
        self.year = ano
        self.category = tipo
#Escriba su respuesta aquí.        


nq2019=Nobel("Chemistry", 2019, "John B. Goodenough")
print(nq2019.category, nq2019.year, nq2019.winner)