#algoritmo1 hola mundo
print("hola mundo")

#algritmo2 mayor o  igual 9
n=0
print("escribir el numero")
n=input()
if (n.isdigit()):
    n=int(n)
    if (n==9):
        print("el numero es 9")
    else:
        if (n>9):
            print("el numero es mayor 9")
        else:
            print("el numero es menor 9")
else:
    print("el numero no es numero")