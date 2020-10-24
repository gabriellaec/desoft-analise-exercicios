def tamanho_collatz(n):
    contador = 1
    while n != 1 :
        if n % 2 == 0 :
            n = n/2
        else :
            n = 3*n + 1
        contador += 1
    return contador

m_inicial = 0
maior_tamanho = 0
m = 1
while m <= 1000 :
    tamanho = tamanho_collatz(m)
    if tamanho > maior_tamanho:
        maior_tamanho = tamanho
        m_inicial = m
    m += 1

print(m_inicial)
