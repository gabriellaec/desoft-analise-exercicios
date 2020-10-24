# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 11:34:49 2019

@author: danie
"""

def calcula_tempo(dic):
    dic2 = {}
    for atleta in dic:
        a = dic[atleta]
        tempo = (200/a)**0.5
        nomedojogador = atleta
        dic2[nomedojogador] = tempo
    return dic2

def qualoatletamaisrapido(calculadora_tempo):
    dicionario = {}
    input1 = input("qual o nome do atleta?")
    while input1 != "sair":
        input2 = int(input("qual a aceleração?"))
        dicionario[input1]=input2
        input1 = input("qual o nome do atleta?")
    dicionario_nomes_e_tempos = calculadora_tempo(dicionario)

    minimo =  1000000
    for i in dicionario_nomes_e_tempos:
        tempo =dicionario_nomes_e_tempos[i]
        if tempo < minimo:
            minimo = tempo
            nome =i
    return [nome, minimo]
maisrapido = qualoatletamaisrapido(calcula_tempo)
print("O vencedor é {0} com tempo de conclusão de {1} s".format(maisrapido[0], maisrapido[1]))