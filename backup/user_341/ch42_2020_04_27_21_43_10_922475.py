palavra = []
while True:

    a = input("Palavra: ")
    if a == "fim":
        break
    palavra.append(a)

print(palavra)
for i in palavra:
    if i[0] == "a":
        print(i)

