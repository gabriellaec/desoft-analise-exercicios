dic={'janeiro':1, 'fevereiro':2, 'março':3, 'abril':4, 'maio':5, 'junho':6, 'julho':7, 'agosto':8, 'setembro':9, 'outubro':10, 'novembro':11, 'dezembro':12}
perg=input('mês:')
if perg in dic:
    j=dic[perg]
    print('o Mês de {0} corresponde a {1}'. format(perg, j))
else:
    print('a palavra não é um mês')