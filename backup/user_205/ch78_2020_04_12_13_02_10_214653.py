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
        calcula_tempo(dicionario) 
        a = 1

vencedor = " "
tempo = 0
for chave,valor in dicionario.items():
    if tempo<valor:
        vencedor = chave
        tempo = valor
print ("O vencedor da porra loca é {0} com o tempo {1}".format(vencedor,tempo))
      
         
       
    