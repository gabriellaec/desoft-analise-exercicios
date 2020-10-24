def soma_valores(lista):
  soma = 0
  for numero in lista:
    soma += numero
  return soma

def soma_impares(lista):
    i = 0
    lista2 = []
    while i < len(lista):
        if lista[i]%2 != 0:
            lista2.append(lista[i])
        i += 1
        
    return soma_valores(lista2)
         
            
            