with open('churras.txt','r') as arquivo:
    conteudo = arquivo.readlines()
total = 0
for strings in conteudo:
    palavra = strings.split(",")
    for info in palavra:
        conta = info[1]*info[2]
        total += conta
print(total)
        