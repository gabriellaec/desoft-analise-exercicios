a=input("digite nomes")
lista=[]
while a != "fim":
    if a not in lista:
        lista.append(a)
    else:
        v=1
    if a+f"{v}"not in lista:
        lista.append(a+f"{v}")
    else:
        v+=1
    
