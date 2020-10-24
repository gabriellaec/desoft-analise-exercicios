def estritamente_crescente(n):
    lista_retornada = []
    i = 0
    tamanho = len(n)
    if tamanho > 0:
        lista_retornada.append(n[0])
        primeiro_termo = lista_retornada[0]
        i = 1
        while i < tamanho:
            if n[i] > primeiro_termo:
                lista_retornada.append(n[i])
                primeiro_termo = n[i]
                i = 2
                while i < tamanho:
                    if n[i] > primeiro_termo:
                        primeiro_termo = n[i]
                        lista_retornada.append(primeiro_termo)
                    i += 1
            i += 1
    return lista_retornada
        

