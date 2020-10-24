def calcula_num_primo(numero):
    i = 1
    cont1 = 0
    while i <= numero:
        if numero % i == 0:
            cont1 += 1
        i += 1  
    if cont1 == 2:
        return True
    else:
        return False
    
    
def maior_primo_menor_que(numero):
    if numero > 1:
        a = 1
        lista = []
        while a <= numero:
            if calcula_num_primo(a):
                lista.append(a)
            a += 1
        i = 0
        maior = lista[0]
        while i < len(lista):
            if maior < lista[i]:
                maior = lista[i]
            i += 1
        return maior
    else:
        return -1