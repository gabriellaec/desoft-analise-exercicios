def  junta_nome_sobrenome(lista_nome,lista_sobrenome):
    
    lista_nome_sobrenome = []
    
    i = 0
    
    while i < len(lista_nome):
        
        
        lista_nome_sobrenome.append(lista_nome[i] +" "+ lista_sobrenome[i] )
        
        
        i = i + 1 
    
    return lista_nome_sobrenome  