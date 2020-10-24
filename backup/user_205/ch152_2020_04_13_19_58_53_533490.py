def verifica_preco(titulo,dicionario,cores):
    for livro in dicionario:
        if livro == titulo:
            cor = dicionario[livro]
    for items in cores:
        if items == cor:
            valor = cores[items]
    return valor 
        
            
        