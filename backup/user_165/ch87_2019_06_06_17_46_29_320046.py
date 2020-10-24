with open("churras.txt","r",encoding = "utf8") as arquivo:
    conteudo = arquivo.read()
dict = {}
for nome in arquivo:
    for quantidade in nome:
        for valor in quantidade:
            dict[0] = nome
            dict[nome] = quantidade
            dict[nome][quantidade] = valor
i = 0
valor_churrasco = 0
while i <=len(dict):
    valor_churrasco = dict[i]*dict[i+1]
    i+=1
print(valor_churrasco)
