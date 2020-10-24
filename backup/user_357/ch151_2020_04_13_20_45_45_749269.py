def classifica_lista(lista):
    lista_tipos = []
    tipo = 0
    n = len(lista)
    i = 0
    j = 1
    iterador_lista = 0 
    posição_lista = 1
    resultado = 0
    while i  < n:
        while j < n:
            if lista[i] > lista[j]:
                tipo = "decrescente"
            elif lista[i] == lista[j]:
                tipo = "nenhum"
            else:
                tipo = "crescente"
            lista_tipos.append(tipo)
            j+=1
        i+=1
    while posição_lista < len(lista_tipos):
         if lista_tipos[iterador_lista] == lista_tipos[posição_lista] and lista_tipos[iterador_lista] == "decrescente":
             resultado = "decrescente"
         elif lista_tipos[iterador_lista] == lista_tipos[posição_lista] and lista_tipos[iterador_lista] == "crescente":
             resultado = "crescente"
         else: 
             resultado = "nenhum"
         posição_lista += 1
         
    return resultado