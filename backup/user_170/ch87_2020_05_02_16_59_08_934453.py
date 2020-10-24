with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.read()
virgula = conteudo.replace('\n',',')
splitted = virgula.split(',')
print(splitted)
custo = 0
i = 1
while i <len(splitted):
    custo += splitted[i]*splitted[i+1]
    i += 3
print(custo)