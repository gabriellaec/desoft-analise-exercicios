def monta_dicionario(primeira, segunda):
        dicionario={}
        if len(primeira) == len(segunda):
            for e, k in zip(primeira, segunda):
                    dicionario[e]=k
        else:
            print('invalido')
        return dicionario
primeira=[1,2,3]
segunda=['q','w','r']
print(monta_dicionario(primeira, segunda))

    