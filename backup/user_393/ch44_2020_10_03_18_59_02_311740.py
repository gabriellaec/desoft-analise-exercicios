lista= [0,'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
x= input("Mês:")
i=0
while i < len(lista):
    if x== lista[i]:
        print("{0}".format(i+1))
 
    i= i + 1
    
 