def eh_primo(numero):   
    i=3
    if numero==0 or numero==1:       
        return False  
    if numero==2:
        return True 
    if numero%2==0: 
        return False 
    while numero>i:
        if numero%i==0:          
            return False       
        i+=2    
    return True 


def verifica_primos(lista):
    i=0
    dic={}
    while i<len(lista):
        dic[lista[i]]=lista[i]
        if eh_primo(lista[i])==True:
            dic[lista[i]]=True
        else:
            dic[lista[i]]=False
        i+=1
    return dic
    