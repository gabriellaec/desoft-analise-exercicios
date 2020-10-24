
def quantos_uns(numero):
    i = 0
    numero = str(numero)
    quantidade = 0
    while i < len(numero):
        if numero[i] == '1':
            quantidade += 1
            i += 1
        else:
            i += 1
    return quantidade

escolha = int(input('Escolha um número: '))
b = quantos_uns(escolha)            

print('O número de uns é {0}'.format(b))