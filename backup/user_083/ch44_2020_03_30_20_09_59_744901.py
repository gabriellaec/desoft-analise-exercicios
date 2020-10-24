meses=['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho','agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
num=(input('digite um mes: '))
i=0
while i<=len(meses):
    if num == meses[i]:
        print(i+1)
        break
    i+=1