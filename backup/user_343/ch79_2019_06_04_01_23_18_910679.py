a=[10, 2, 3]
b=[13, 3, 3]
def monta_dicionario(a,b):
    dict={}
    for k in a:
        for i in b:
            dict[k]=i
    return dict   
    