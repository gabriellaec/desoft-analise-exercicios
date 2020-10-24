def subtracao_de_listas():
    lista1=[2, 7, 3.1, 'banana']
    lista2 = [2, 'banana', 'carro']
    nova_l=[]
    i=0
    while lista1[i]<len(lista2):
        if i  not in lista2:
            nova_l.append(i)
            i+=1
        i+=1
    return nova_l
        
    
    