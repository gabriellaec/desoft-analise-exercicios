def verifica_progressao(S):
    #Teste para ver se é P.A.:
    PA = True
    for i in range(0,len(S)-3):
        if S[i + 1] - S[i] != S[i + 2] - S[i + 1]:
            PA = False
            break
    #Teste para ver se é P.G.:
    PG = True
    for j in range(0,len(S)-3):
        if S[i + 1] / S[i] != S[i + 2] / S[i + 1]:
            PG = False
            break
    if PA and PG:
        return "AG"
    if PA and not PG:
        return "PA"
    if PG and not PA:
        return "PG"