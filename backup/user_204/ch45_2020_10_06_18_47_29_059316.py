lista = []
novo_valor = float(input("Digite um valor: "))
while novo_valor != 0 and novo_valor > 0:
    lista.append(novo_valor)
    novo_valor = float(input("Digite um valor: "))
lista.reverse()
print(lista)