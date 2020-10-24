def interseccao_chaves(primeira, segunda):
        lista=[]
        for e in (primeira.keys()):
            if e in segunda.keys():
                lista.append(e)
        return lista
primeira={'a':1, 'q':3, 'r':8}
segunda={'b':4, 'c':3, 'r':8}
print(interseccao_chaves(primeira, segunda))
