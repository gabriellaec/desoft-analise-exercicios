mes = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

num = int(input('digite um numero: '))

if num>0 and num<13:
    mess = mes[num-1]
    print(mess)