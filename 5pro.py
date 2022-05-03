r=input("ingrese el radio")
h=input("ingrese la altura")
if (r.replace(".","",1).isdigit() and h.replace(".","",1).isdigit()):
    r=float(r)
    h=float(h)
    if (r<=0 or h<=0):
        print("los números tienen que ser mayores a 0")
    else:
        area=(2*3.14*r*h)+(2*3.14*r*r)
        volumen=(3.14*r*r*h)
        print("el area es",area)
        print("el volumen es",volumen)
else:
    print("ingrese numeros validos")