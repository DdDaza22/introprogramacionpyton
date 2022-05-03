a=int(input("ingrese un número"))
b=int(input("ingrese un número"))
c=int(input("ingrese un número"))
if (a>=b):
    if (c>=a):
        print(f"el orden es {c} {a} {b}")
    elif (c<=b):
        print(f"el orden es {a} {b} {c}")
    else:
        print(f"el orden es {a} {c} {b}")
else:
    if (c>=b):
        print(f"el orden es {c} {b} {a}")
    elif (c<=a):
        print(f"el orden es {b} {a} {c}")
    else:
        print(f"el orden es {b} {c} {a}")