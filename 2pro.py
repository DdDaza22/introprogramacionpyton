n=int(input("ingrese un número"))
div=2
band=True
if (n==1) :
    print("es primo")
else:
    while (band==True and (n>div)):
        if(n%div==0):
            band=False
        div=div+1
    if (band==True):
        print("es primo")
    else:
        print("no es primo")
