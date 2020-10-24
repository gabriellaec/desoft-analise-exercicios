def soma_elementos(valores) :
    s= 0
    h= 0
    while h < len(valores) :
        s += valores[h]
        h += 1 
    return s



lista =[0]*100
lista[0] = 1
lista[1] = 1/2
i = 0
while i <  99 :
     lista[i + 1] = lista[i]*(1/2)
     i = i + 1

resultado = soma_elementos(lista)
print(resultado)
