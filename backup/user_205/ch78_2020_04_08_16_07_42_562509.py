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
    nome = input("Fala ae querido: ")
    if nome == "sair":
        print(calcula_tempo(dic))
        a = 1
    else:
        aceleracao = int(input("Só nao pode ser a da luz: "))
        dic[nome]=aceleracao
         
         
       
    