mes = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
nom=str(input("Digite o nome do mês: "))
procura = True
i=0
while procura:
    if mes[i]==nom:
        num = i + 1
        procura = False
    else:
        i+=1
print (num)