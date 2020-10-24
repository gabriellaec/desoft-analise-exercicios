def lista_sufixos(palavra):
    lista = []
    contador = 0
    for e in palavra:
        sufixo = [contador:]
        contador += 1
        lista.append(sufixo)
    return lista
        
        