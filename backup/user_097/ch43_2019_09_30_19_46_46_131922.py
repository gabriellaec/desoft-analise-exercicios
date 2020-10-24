def sequenciaCollatz (n):
    sequencia =[]
    sequencia.append(n)
    while (n != 1):
        if (n%2==0):
            n = (n/2)
            sequencia.append(n)
        elif (n%2!=0):
            n = ((3*n)+1)
            sequencia.append(n)
    return sequencia

numero = 1
maior = 0
numeroProduz = 0

while (numero<=1000):

    tamanhoLista = len(sequenciaCollatz(numero))
    print(numero, tamanhoLista)

    if (tamanhoLista>maior):
        maior = tamanhoLista
        numeroProduz = numero
    numero = numero + 1

print(numeroProduz)