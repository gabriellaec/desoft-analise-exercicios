with open("churras.txt","read",encoding = "utf8") as arquivo:
    conteudo = arquivo.read()
dict = {}
for nome,quantidade,valor in arquivo:
    dict[0] = nome
    dict[nome] = quantidade
    dict[nome][quantidade] = valor
i = 0
valor_churrasco = 0
while i <=len(dict):
    valor_churrasco = dict[i]*dict[i+1]
   	i+=1
print(valor_churrasco)
