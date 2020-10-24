def eh_par_impar(x):
    if x % 2 == 0:
        return x/2
    else: 
        return 3*x + 1 



def collatz(num):
    lista = [num]
    while True:
        a = eh_par_impar(num)
        lista.append(a)
        if a == 1:
            break 
        num = a 
    return len(lista)

lista_tamanho = []
i = 0
while i < 1000:
    lista_tamanho[i] = collatz(i)
    i += 1

print(max(lista_tamanho))
