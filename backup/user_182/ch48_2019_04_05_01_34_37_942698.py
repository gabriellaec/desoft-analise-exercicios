meses=[0]*12
meses=["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
mes=input('digite o nome do mês: ')
while not mes in meses:
    print('inválido')
i=0
while i<len(meses):
    if meses[i]==mes:
        print("{0}".format(i+1))
        break
    i+=1