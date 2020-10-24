def verifica_primos(lista):
    tot=0
    i=0
    dict = {}
    while i < (len(lista)-1):
        if lista[i]%i ==0:
            tot+=1
                
        else:
            tot=tot
            
    return tot
primo =True
if tot ==2:
    print("{0} é primo".format(lista[i])
    dict[lista[i]] = True
else: 
    print("{0} não é primo.".format(lista[i])
    dict[lista[i]] = False
          
          
print(dict)