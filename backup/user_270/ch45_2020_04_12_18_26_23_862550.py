lista = []
per = 1
while per > 0 :
    per = int(input("Digite um inteiro positivo"))
    if per > 0 :
        lista.append(per)
lista.reverse()
print(lista)