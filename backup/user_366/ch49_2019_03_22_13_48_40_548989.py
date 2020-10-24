lista = []
pede_num = int(input("digite um número inteiro: "))

while pede_num > 0:
    lista.append(pede_num)
    pede_num = int(input("digite outro número inteiro: "))

print(lista[ : : -1])