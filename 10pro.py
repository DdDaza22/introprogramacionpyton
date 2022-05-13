p1 = "hola"
print("Adivine la palabra: ")
while True:
    p2 = input().lower() #para ponerlo todo en minuscula
    if p2 == p1:
        break 
    print("Vuelve a intentarlo: ")
print("Felicidades, has adivinado la palabra")
