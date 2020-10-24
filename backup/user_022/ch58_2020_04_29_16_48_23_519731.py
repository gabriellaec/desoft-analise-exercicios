def conta_a(palavra):
    numero_a = []
    palavra = input('Digite uma palavra: ')
    i = 0
    n = len(palavra)
    while i<n:
        if palavra[i]=='a':
            numero_a.append(palavra[i])
    return numero_a
            