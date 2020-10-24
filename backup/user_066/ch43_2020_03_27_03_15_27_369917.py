meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outrubro', 'novembro', 'dezembro']
x = int(input())
for i in range(len(meses)):
    if x == i+1:
    	print meses[i]
