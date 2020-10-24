numeros_positivos = []
nova_lista = []
numero_escolhido = int(input())

while numero_escolhido > 0:
    numeros_positivos.append(numero_escolhido)
    numero_escolhido = int(input())
    
i = 0
while i < len(numeros_positivos):
    nova_lista.append(numeros_positivos[len(numeros_positivos) - i - 1])
    i += 1

print(nova_lista)