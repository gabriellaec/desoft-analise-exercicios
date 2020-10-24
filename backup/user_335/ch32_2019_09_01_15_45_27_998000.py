# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 12:30:51 2019

@author: User
"""

pergunta = True

while pergunta:
    resposta = input("Você possui dúvidas na disciplina? ")
    if resposta != "não":
        print ("Pratique mais")
        resposta = input("Você possui dúvidas na disciplina? ")
    else:
        print ("Até a próxima")
        pergunta = False