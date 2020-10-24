i = 0
lista = [0]
while lista[i] != "fim" :
    per =input("Digite uma palavra: ")
    if per[0] == "a" :
        lista[i] = per
        i += 1
t = 0
while t < len(lista):
    print(lista[t])
    t +=1
        