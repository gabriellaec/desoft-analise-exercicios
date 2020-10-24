def quantos_uns(número):
    z = str(número)
    contador = 0
    soma = 0 
    tamanho = len(número)
    while contador < tamanho:
        if z [contador] == "1":
            soma += 1
        contador += 1
    return soma
            
            