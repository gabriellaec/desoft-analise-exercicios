meses_nome = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novombro', 'dezembro']
resposta= input("Qual o nome do mês? ")

for i in meses_nome:
    if resposta == i:
        print(meses_nome.index(i)+1)