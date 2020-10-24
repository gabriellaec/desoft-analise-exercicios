numero = int(input('Digite o primeiro número: '))
i = 1
lista = []
atsil = []
while numero > 0:
    lista.append(numero)
    numero = int(input('Digite o próximo número: '))
print('>>>> lista: {} '.format(lista))

while i <= len(lista):
    atsil.append(lista[(len(lista) - i)])
    i += 1
print('>>>> atsil: {}'.format(atsil))



