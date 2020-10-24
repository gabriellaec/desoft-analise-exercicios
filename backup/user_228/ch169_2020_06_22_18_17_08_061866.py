string=""
lista=[]
while string!="fim":
    if string not in lista:
        lista.append(string)
    else:
        v=1
    while True:
        if string+f"{v}" not in lista:
            lista.append(string+f"{v}")
        else:
            v+=1
            
print(lista)
            
    
