
lista_mes = [0]*13
lista_mes [1] = "Janeiro"
lista_mes [2] = "Fevereiro"
lista_mes [3] = "Março"
lista_mes [4] = "Abril"
lista_mes [5] = "Maio"
lista_mes [6] = "Junho"
lista_mes [7] = "Julho"
lista_mes [8] = "Agosto"
lista_mes [9] = "Setembro"
lista_mes [10] = "Outubro"
lista_mes [11] = "Novembro"
lista_mes [12] = "Dezembro"

mês=input("Qual é o nome do mês")

contador=1


while contador<=12:
    contador+=1
    if lista_mes[contador]==mês:
        print (contador)
        
    


