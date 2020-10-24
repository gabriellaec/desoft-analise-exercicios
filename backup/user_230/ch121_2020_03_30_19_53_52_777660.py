def subtracao_de_listas (l1, l2):
    contador_l1=0
    l3=[]
    while contador_l1<len(l1):
        if l1[contador_l1] in l2:
            l3.append(l1[contador_l1])
        contador_l1+=1
    return l3
    
               

lista1=[2, 7, 3.1, "banana"]
lista2=[2, "banana", "carro"]