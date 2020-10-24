import random
i=100
print(i)
aposta=int(input("valor"))
while aposta>0 or i >0:
    x=input("qual aposta?(n/p)")
    if x=="n":
        numero=int(input("numero"))
        j=random.randint(0,36)
        if numero==j:
            i+=35*aposta
        else:
            i=i-aposta
    else:
        k=input("numero? (p/i)")
        r=random.randint(0,36)
        if k == "p"and r % 2==0 or k =="i" and r % 2!=0:
            i+=aposta
        else:
            i=i-aposta
    print(i)
    aposta=int(input("valor"))