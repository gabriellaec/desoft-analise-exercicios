a="digite nomes"
v=1
lista=[]
while a != "fim":
    if a not in lista:
        lista.append(a)
    else:
        lista.append(a+f"{v}")
    
