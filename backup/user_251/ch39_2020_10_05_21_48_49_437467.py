
numero_ini = 999
maior_tamanho = 0
while numero_ini > 1:
    numero = numero_ini
    tamanho = 0
    while numero != 1:
        if numero % 2 == 0:
            numero = numero/2
            tamanho += 1
        else:
            numero = (numero*3)+1
            tamanho += 1

     
    if tamanho > maior_tamanho:
        maior_tamanho = numero_ini
    
    numero_ini -= 1
    
print(maior_tamanho)