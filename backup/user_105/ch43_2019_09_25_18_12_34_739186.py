def colinz(meu_numero):
    i = 1
    vezes = [1]
    while meu_numero != 1:

        if meu_numero%2 == 0:
            meu_numero = meu_numero/2
            vezes.append(i)
            
        elif meu_numero%2 != 0:
            meu_numero = (meu_numero*3)+1
            vezes.append(i)
            
    return len(vezes)
print(colinz(179))

for i in range(1,1001):
    maior = colinz(1)
    if colinz(i) > maior:
        maior = colinz(i)
        n = i