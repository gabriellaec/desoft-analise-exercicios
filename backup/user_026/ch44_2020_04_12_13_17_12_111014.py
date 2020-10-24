nome_meses=['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
resposta = input("Qual o nome do mes?")

for i in nome_meses:
    if resposta == i:
        print(nome_meses(i)+1)