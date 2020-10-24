
def subtracao_de_listas(lista_1, lista_2):
    ''' retorna uma lista com os valores da "lista_1"
        não presentes também na "lista_2" '''
    
    # define a lista a que os valores serão adicionados
    lista_final = list()
    
    # índice de contagem para a comparação dos elementos
    # no loop while
    indice_1 = 0
    
    # loop de checagem (percorre os valores da "lista_1")
    while True:
                
        # elemento verificado no loop
        elemento = lista_1[indice_1]
        
        # índice de checagem para o loop da "lista_2"
        indice_2 = 0
        
        # loop de comparação (percorre os valores da "lista_2")
        while True:
            
            # verifica se a "lista_2" já foi percorrida por inteiro
            # nesse caso, adicionar "elemento" à "lista_final"
            if indice_2 == len(lista_2): lista_final.append(elemento)
            
            # checagem
            elif elemento == lista_2[indice_2]: break
                
            # incremento do "indice_2"
            indice_2 += 1
       
        # incremento do "indice_1"
        indice_1 += 1
    
    # retorna a lista completa
    return lista_final
    
    
    
    