def calcula_tempo (lista):
    dic={}
    for nome,aceleracao in lista.items():
        tempo=((200)**(1/2))/(aceleracao**(1/2))
        dic[nome]=tempo
    return dic