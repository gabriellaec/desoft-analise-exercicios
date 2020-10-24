def verifica_progressao(seq):
    PA = False
    PG = False

    # Verifica se é PA
    delta = [ seq[idx] - seq[idx-1] for idx,n in enumerate(seq) ]
    del(delta[0])
    deltaBool = [ delta[idx] == delta[idx-1] for idx,n in enumerate(delta) ]
    for b in deltaBool:
        if not b:
            PA = False
            break
        else:
            PA = True

    # Testa se a lista possui zero e verifica se é PG
    if 0 not in seq:
        quoc = [ seq[idx] / seq[idx-1] for idx,n in enumerate(seq) ]
        del(quoc[0])
        quocBool = [ quoc[idx] == quoc[idx-1] for idx,n in enumerate(quoc) ]
        for b in quocBool:
            if not b:
                PG = False
                break
            else:
                PG = True
    else:
        for n in seq:
            if n != 0:
                PG = False
                break
            else:
                PG = True

    # Retonar string indicando se é PA, PG, ambos ou nenhum        
    if PA and PG:
        return "AG"
    elif PA:
        return "PA"
    elif PG:
        return "PG"
    return "NA"

# PA = [1,2,3,4]
# PA2 = [4,3,2,1]
# PG = [1,2,4,8]
# PG2 = [81,-27,9,-3]
# AG = [1,1,1,1]
# NA = [2,1,1,3]
# ZERO = [0,0,0,0]
# print(verifica_progressao(PA))
# print(verifica_progressao(PA2))
# print(verifica_progressao(PG))
# print(verifica_progressao(PG2))
# print(verifica_progressao(AG))
# print(verifica_progressao(NA))
# print(verifica_progressao(ZERO))
