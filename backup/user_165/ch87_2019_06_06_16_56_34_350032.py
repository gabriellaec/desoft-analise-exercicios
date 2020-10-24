with open("churras.txt","read",encoding = "utf8") as arquivo:
    conteudo = arquivo.read()
dict = {}
for nome,quantidade,valor in arquivo:
    dict[0] = nome
    dict[nome] = quantidade
    dict[nome][quantidade] = valor
valor_churrasco = dict[0]*dict[0][1]
