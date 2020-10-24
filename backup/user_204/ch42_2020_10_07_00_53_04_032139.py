palavra = 0
nova = []
while palavra != "fim":
    palavra = input("Qual a palavra? ")
    if palavra[0] == "a":
        nova.append(palavra)

i = 0
while i < len(nova):
    print(nova[i])
    i += 1