mes= ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro','outubro','novembro','dezembro']
n= [1,2,3,4,5,6,7,8,9,10,11,12]
i= 0
a= input('Qual o mês? ')
while i<len(n):
    if a == mes[i]:
        print(n[i])
    i += 1