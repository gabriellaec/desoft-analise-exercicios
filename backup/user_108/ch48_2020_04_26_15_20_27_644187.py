def eh_crescente(lista):
    numeros = [v for i, v in enumerate(lista) if i == 0 or v != lista[i-1]]
    return lista == sorted(list(dict.fromkeys(lista)))