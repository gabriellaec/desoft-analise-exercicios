mes = input('Qual é o nome do mês? ')
num = [1,2,3,4,5,6,7,8,9,10,11,12]
lista = ["janeiro", "fevereiro", "março","abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
i = 0 
while i< len(lista):
    if mes == lista[i]:
        print(lista[i].index)
    i+=1
