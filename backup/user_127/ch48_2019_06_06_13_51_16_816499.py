lista = ["jan", 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'sete', 'out', 'nov', 'dez']
p = input("mes? ")
for i in range(len(lista)):
    if p == lista[i]:
        print(i+1)