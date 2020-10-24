def faixa_notas(lista):
    #quantos alunos possuem notas inferior a 5
    #quantos possuem notas de 5 até 7
    #quantos possuem notas maior que 7
    i= 0
    cont1 =0
    cont2 = 0
    cont3 = 0
    lista_nova = []
    while i<len(lista):
        if lista[i]>= 0 and lista[i] <5:
            cont1+=1
            lista_nova.append(cont1)
        elif lista[i]>=5  and lista[i]<=7:
            cont2+=1
            lista_nova.append(cont2)
        elif lista[i]>7  and lista[i]<=10:
            cont3+=1
            lista_nova.append(cont3)
        i+=1
        return lista_nova

    
