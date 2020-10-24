i=100
print(i)
aposta=int(input("valor"))
while aposta>0:
    x=int(input("qual aposta?(n/p)"))
    if x=="n":
        numero=int(input("numero"))
        j=ramdom.randint(1,36)
        if numero==j:
            i+=35*aposta
        else:
            i=i-aposta
    else:
        k=int(input("numero"))
        r=ramdom.randint(1,36)
        if k % 2==0 and r % 2==0 or k % 2 !=0 and r % 2!=0:
            i+=aposta
        else:
            i=i-aposta
    aposta=int(input("valor"))
        