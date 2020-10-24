dic = {}
nome = input("Nome ")

while(nome != 'sair'):
    velo = int(input("Velo "))
    dic[nome] = velo
    nome = input("Nome ")

def calcula_tempo(dic):
    for nome in dic:
        v = dic[nome]
        t = (100/v)
        dic[nome] = t
    menor = 1000000000000000000
    for nome in dic:
        if dic[nome] < menor:
            menor = dic[nome]
            primeiro = nome
    return "O vencedor é {0} com tempo de conclusão de {1} s".format(primeiro, dic[primeiro])

print(calcula_tempo(dic))