def Fac(N):
    if N<1:
        raise
    if N==1:
        return 1
    else:
        print('return{} Factorial ({}-1)'.format(N,N))
        return N * Fac(N-1)
n=input("el numero")
try:
    n=int(n)
    r=Fac(n)
    print(r)
except TypeError:
    print('error de tipo')
except:
    print('error')
