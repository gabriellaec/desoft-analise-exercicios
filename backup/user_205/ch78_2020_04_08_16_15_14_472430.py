from math import sqrt 
def calcula_tempo(dicionario):
    resultado = {}
    for nomes in dicionario.keys():
        for aceleracao in dicionario.values():
            resultado[nomes]=(sqrt(200/dicionario[nomes]))
    return resultado
a = 0
while a!= 1:
    dic={}
    nome = input("Fala ae: ")
    if nome == "sair":
        resultado=calcula_tempo(dic)
        for nome in resultado.keys():
            for tempo in resultado.values():
                print('O vencedor é {0} com tempo de conclusão de TEMPO {1}'.format(resultado[nome],resultado[min(tempo)]
                a = 1
    else:
        aceleracao = int(input("Qual a aceleração?: "))
        dic[nome]=aceleracao
         
         
       
    