def total_do_semestre_por_bairro(t):

    t = dict()
    lista_numeros_semestre = []
    len(lista_numeros_semestre) == 6
    
    for i in range(1,13):
        t[(f'Bairro {i}')] = lista_numeros_semestre[i]
        for j in range(len(lista_numeros_semestre)):
            total = sum(lista_numeros_semestre[j])
            t2 = dict()
            t2[(f'Bairro{i}')] = total
            return t2
        
        