#descobrir o tamanho da sequencia
def tamanho_collatz(n):
    contador = 1 #contador = 0 é n
    while n != 1 :
        if n % 2 == 0 :
            n = n/2
        else :
            n = 3*n + 1
        contador += 1 #vai somando ao contador cada vez que é feita a verificaçao do valor do n(se é par ou impar)
    return contador

m_inicial = 0
maior_tamanho = 0
m = 1
while m <= 1000 :
    tamanho = tamanho_collatz(m) # vai criar uma lista em coluna no terminal com todos os valores de m sendo o argumento(m varia de 1 ate 1000) da funcao tamanho_collatz
    if tamanho > maior_tamanho:   # essa condiçao vai ser usada para encontrarmos o contador de maior valor
        maior_tamanho = tamanho
        m_inicial = m # m_inicial vai receber o argumento que tem o maior contador
    m += 1

print(m_inicial)
