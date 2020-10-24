def seq(n):
    lista = []
    while n > 1:
        if n%2 == 0:
            n = n/2
            lista.append(n)
        else:
            n = 3*n + 1
            lista.append(n)
    return len(lista)

n1 = 1
num = 0
n_maior = 0
while n1 < 1000:
    tamanho = seq(n1)
    if tamanho > num:
        num = tamanho
        n_maior = n1
    n1+=1
print(n_maior)