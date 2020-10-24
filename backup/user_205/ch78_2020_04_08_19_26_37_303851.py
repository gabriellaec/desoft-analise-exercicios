from math import sqrt 
def calcula_tempo(dicionario):
    resultado = {}
    for nomes in dicionario.keys():
        for aceleracao in dicionario.values():
            resultado[nomes]=(sqrt(200/dicionario[nomes]))
    return resultado
a = 0
dic={}
while a!= 1:
    nome = input("Fala ae: ")
    if nome == "sair":
        resultado=calcula_tempo(dic)
        y = 0
        cidadao = " "
        for nome,valor in resultado.items():
            if y == 0 or y < valor: 
                y = valor
                cidadao=nome
        print ('O vencedor é {0} com tempo de conclusão de TEMPO {1}'.format(cidadao,y))
        break
    else:
        aceleracao = int(input("Qual a aceleração?: "))
        dic[nome]=aceleracao
         
         
       
    