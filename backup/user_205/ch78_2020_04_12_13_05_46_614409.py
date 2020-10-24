from math import sqrt
def calcula_tempo(dicionario):
    resultado = {}
    for nomes in dicionario.keys():
        for aceleracao in dicionario.values():
            resultado[nomes]=(sqrt(200/dicionario[nomes]))
    return resultado
a = 0
dicionario = {} 
while a!=1: 
    pergunta = input("Qual el nombre del cidadón: ")
    if pergunta != "sair":
        acelera = int(input("Qual foi a ac do mano: "))
        dicionario[pergunta]=acelera
    else:
        resultado = calcula_tempo(dicionario) 
        a = 1

vencedor = " "
tempo = 0
for chave,valor in resultado.items():
    if tempo<valor:
        vencedor = chave
        tempo = valor
print ("O vencedor é {0} com tempo de conclusão de TEMPO {1} s".format(vencedor,tempo))
      
         
       
    