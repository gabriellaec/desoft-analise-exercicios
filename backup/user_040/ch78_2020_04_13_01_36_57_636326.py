dicionario = {}
lista = [100,100]
while nome != "sair":
    nome = input("digite um nome: ")
    if nome != "sair":
        aceleração = input("digite uma aceleração: ")
        v2 = 2*aceleração*100
        t = v2**(1/2)/aceleração
        dicionario[nome] = t
for nome,tempo in dicionario.items():
    if tempo < lista[1]:
        lista[0] = nome
        lista[1] = tempo

print ("O vencedor é {0} com tempo de conclusão de {1} s".format(lista[0],lista[1]))
        