MESES = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
NOME = input('Qual o nome do mês?')
IND = -1
i = 0
while i < len(MESES):
    if MESES[i] == NOME:
        IND = i
    i += 1
if IND == -1:
    print('Mês invalido')
else:
    print(IND+1)

    