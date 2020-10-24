mes = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']

num = int(input('digite um numero: '))

if num>0 and num<13:
    mess = mes[num-1]
    print(mess)