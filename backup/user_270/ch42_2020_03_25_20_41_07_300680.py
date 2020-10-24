per = ""
lista = []
while per != "fim":
    per =input("Digite uma palavra: ")
    if len(per) > 0 and per[0] == "a" :
        lista.append(per)
t = 0
while t < len(lista):
    print(lista[t])
    t +=1
        