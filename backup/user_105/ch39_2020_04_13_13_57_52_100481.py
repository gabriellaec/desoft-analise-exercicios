def colinz(meu_numero):
    vezes = []
    while meu_numero != 1:

        if meu_numero%2 == 0:
            meu_numero = meu_numero/2
            vezes.append(meu_numero)            
        else:
            meu_numero = (meu_numero*3)+1
            vezes.append(meu_numero)
            
    return len(vezes)

maior = 0
for i in range(1,1000):
    if colinz(i) > maior:
        maior = colinz(i)
        n = i
print(n) 