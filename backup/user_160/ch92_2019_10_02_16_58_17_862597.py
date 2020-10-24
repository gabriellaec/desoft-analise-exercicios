def simplifica_dict(dicionario):
    for k,v in dicionario.items():
        l = []
        i=0
        while i < len(dicionario):
            if dicionario [i] not in l:
                l.append(dicionario[i])
            print(l)
        
        