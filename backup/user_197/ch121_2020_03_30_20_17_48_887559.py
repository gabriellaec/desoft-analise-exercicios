def subtracao_de_listas(l1,l2):
    l3=[]
    l1_counter=0
    while l1_counter<len(l1):
        if l1[l1_counter] not in l2:
            l3.append(l1[l1_counter])
        l1_counter+=1
    return l3
lista1 = [2, 7, 3.1, 'banana']  
lista2 = [2, 'banana', 'carro']
print(subtracao_de_listas(lista1, lista2))