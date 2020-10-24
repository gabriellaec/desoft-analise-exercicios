lista = []
per = 1
while per > 0 :
    per = int(input("Digite um inteiro positivo"))
    if per > 0 :
        lista.append(per)
i = 1
while i < len(lista) + 1:
    lista[len(lista) - i] = lista[i-1]
    i += 1
print(lista)