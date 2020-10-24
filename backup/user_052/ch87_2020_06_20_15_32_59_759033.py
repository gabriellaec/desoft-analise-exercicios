with open ("churras.txt", "r") as arquivo:
    ler = arquivo.read()
    a =  ler.split()
    i = 1
    soma = 0
    while i < len(a):
        soma += a[i] * a[i+1]
        i += 3
    return soma