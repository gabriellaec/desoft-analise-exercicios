def quantos_uns(numero):
    z = str(numero)
    contador = 0
    soma = 0
    tamanho = len(numero)
    while contador < tamanho:
        if z[contador] == "1":
            soma += 1
        contador += 1
    return soma        
             
  