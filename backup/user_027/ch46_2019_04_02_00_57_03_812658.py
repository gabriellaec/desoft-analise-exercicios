lista = []
i = input("Digite uma palavra: ")
while i != "fim":
  i = input("Digite outra palavra: ")
  lista.append(i)
for i in lista:
  if i[0] == "a":
    print(i)
