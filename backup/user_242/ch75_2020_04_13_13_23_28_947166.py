def verifica_primos(lista):
    tot=0
    i=0
    dicionario = {}
    while i < (len(lista)-1):
        if lista[i]%i ==0:
            tot+=1        
        else:
            tot=tot
        i+=1
    return tot
primo =True
if tot ==2:
    print("{0} é primo".format(lista[i])
    dicionario[lista[i]] = True
else: 
    print("{0} não é primo.".format(lista[i])
    dicionario[lista[i]] = False
          
          
print(dicionario)