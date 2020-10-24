def calcula_tempo(dicat):
    novodic={}
    for nome,ace in dicat.items():
        novodic[nome]=((200/ace)**(1/2))
    return novodic