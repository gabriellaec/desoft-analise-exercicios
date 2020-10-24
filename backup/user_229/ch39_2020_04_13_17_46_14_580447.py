def sequencia(n):
    lista = [n]
    i = 0
    while lista[i] != 1:
        if lista[i]%2 == 0:
            lista.append(lista[i]/2)
            i += 1
        else:
            lista.append(1+(lista[i])*3)
            i += 1
    return lista
            

def contagem(n):
    return len(sequencia(n))


    
maior = 0

for i in range(1, 1000):
    if contagem(i) > contagem(i-1):
        maior = i
        
print(maior)