def interseccao_valores(primeira, segunda):
        lista=[]
        for e in (primeira.values()):
            if e in segunda.values():
                lista.append(e)
        return lista
primeira={'a':1, 'q':3, 'r':8}
segunda={'b':4, 'c':3, 'r':8}
print(interseccao_valores(primeira, segunda))