def subtracao_de_listas(lista_1, lista_2):
    
    resultado = list()
    
    for elemento in lista_1:
        
        if not elemento in lista_2:
            resultado.append(elemento)
    
    return resultado