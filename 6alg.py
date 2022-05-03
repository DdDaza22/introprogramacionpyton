n=0
n=int(input("escribe numero"))
div=1
while(div<=n):
    if (n%div==0):
        print(div, "es divisor de ",n)
    div=div+1
