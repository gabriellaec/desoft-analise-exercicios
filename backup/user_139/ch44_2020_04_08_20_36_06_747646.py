meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
mes = input ('Digite o mes: ')
i = 0
while i < len(meses):
    if mes == meses[i]:
        print (i + 1)
    i += 1
    
    
dic = {}
dic['janeiro'] = 1
dic['fevereiro'] = 2
dic['março'] = 3
dic['abril'] = 4
dic['maio'] = 5
dic['junho'] = 6
dic['julho'] = 7
dic['agosto'] = 8
dic['setembro'] = 9
dic['outrubro'] = 10
dic['novembro'] = 11
dic['dezembro'] = 12
print (dic)