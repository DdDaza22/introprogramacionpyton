import math
r=input("ingrese el radio")
h=input("ingrese la altura")
pi=math.pi
if (r.replace(".","",1).isdigit() and h.replace(".","",1).isdigit()):
    r=float(r)
    h=float(h)
    if (r<=0 or h<=0):
        print("los números tienen que ser mayores a 0")
    else:
        area=(2*pi*r*h)+(2*pi*r*r)
        volumen=(pi*r*r*h)
        print("el area es",area)
        print("el volumen es",volumen)
else:
    print("ingrese numeros validos")