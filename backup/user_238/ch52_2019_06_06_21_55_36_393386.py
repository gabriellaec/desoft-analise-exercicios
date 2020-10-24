def eh_crescente(lista):
    i=1
    l2=[]
    maior=lista[0]
    while i < len(lista):
        if lista[i] > maior:
            maior=lista[i]
            l2.append(maior)
        i+=1	
    
    if len(lista)-1 == len(l2):
        return True
    else:
        return False
l=[1, 2, 3, 4]
l2=[1,5,2,3]
print(eh_crescente(l))
print(eh_crescente(l2))
        