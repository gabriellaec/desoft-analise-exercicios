lista_mes = [0]*13
lista_mes [1] = "janeiro"
lista_mes [2] = "fevereiro"
lista_mes [3] = "março"
lista_mes [4] = "abril"
lista_mes [5] = "maio"
lista_mes [6] = "junho"
lista_mes [7] = "julho"
lista_mes [8] = "agosto"
lista_mes [9] = "setembro"
lista_mes [10] = "outubro"
lista_mes [11] = "novembro"
lista_mes [12] = "dezembro"

contadori = 1
mes = input("Qual o nome do mês?")

while contadori<= 12:
    if lista_mes[contadori] == mes:
        print(contadori)
    contadori +=1
