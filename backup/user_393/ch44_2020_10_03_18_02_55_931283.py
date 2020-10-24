lista= ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
x= input("Mês:")
i=0
while i < len(lista):
    if lista[i]== x:
        lista[i]= x
        i= i + 1
        
print(lista[i])
        
