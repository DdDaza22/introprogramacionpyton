"""
#ej1
lst1=[1,2,3,4,5]
#lst2=[]
#for n in lst1:
    #lst2.append(n)
lst2=[n for n in lst1 ]
print(lst2)
"""
"""
#ej2
lst2=[]
lst=[]
#for n in range(1200,2001,130):
#    lst.append(n)
#print(lst)
lst=range(1200,2001,130)
for x in lst:
    lst2.append(x)
print(lst2)
"""
dict={"Susuke Ignis": 985, "Chevrolet park Activ": 1100, "Volkswagen CrossUP": 1245, "Masda CX-3": 1254, "Susuki Vitara": 1245, "Nissan Kicks": 1310, "Mazda CX-5": 1672, "Ford Escape": 1625}

lst=[n.upper() for n in dict if dict[n]<1300]



print(lst)