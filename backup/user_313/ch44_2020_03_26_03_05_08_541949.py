meses = ['Inicio','janeiro','fevereiro', 'março', 'abril', 'maio','junho', 'julho','agosto', 'setembro', 'outubro','novembro','dezembro']
numero =['Inicio',1,2,3,4,5,6,7,8,9,10,11,12]

b = input('Qual o nome do mes você esta procurando: ')

a = True
indice = 0

while a:    
    if b == meses[indice]:
        print(numero[indice])
        a = False
    
    else:
        indice = indice + 1