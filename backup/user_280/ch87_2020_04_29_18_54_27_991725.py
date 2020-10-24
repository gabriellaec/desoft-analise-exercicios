with open('cancao_do_exilio.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

custo = 0    
for linha in linhas:
    custo += float(linha[-1])*float(linha[-2])

print(custo)