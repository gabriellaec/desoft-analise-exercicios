def verifica_primos (lista):
    dic={}
    for numero in lista:
        if numero==2 or numero==3:
            dic[numero]=True
        else:
            termos=numero-2
            contador=[0]*termos
            contador[0]=3
    
            if numero%2==0:
                dic[numero]=False
            else:
                i=0
                while contador[i]<numero:
                    contador[i+1]=contador[i]+1

                    if numero%contador[i]==0:
                        dic[numero]=False
                        break
                    elif contador[i+1]==numero:
                        dic[numero]=True
                    i+=1
    return dic
