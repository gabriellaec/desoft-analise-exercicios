with open("macacos-me-mordam.txt","r") as arquivo:
    conteudo = arquivo.read()
lista= conteudo.split(" ")
i=0
soma= 0
while i<len(lista):
    lista.lower()
    if "banana" in lista:
        soma+=1
        i+=1
print(soma)

