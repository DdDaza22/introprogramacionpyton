def Fibo(N):
    if N<2:
        return N
    else:
        return (Fibo(N-1)+Fibo(N-2))

n=int(input("introduzca número"))
if n>0:
    numero=n-1
    actual=Fibo(numero)
    print(actual)