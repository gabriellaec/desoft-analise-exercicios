def eh_crescente(lista):
numeros = [v for i, v in enumerate(your_list) if i == 0 or v != your_list[i-1]]
return lista == sorted(numeros)