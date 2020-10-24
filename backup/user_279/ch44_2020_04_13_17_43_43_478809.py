listames = ["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
listanumero = ["1","2","3","4","5",'6','7','8','9','10','11','12']
def dicionariomes(x,y):
    dicionario = {}
    for e in range(len(x)):
        dicionario[x[e]] = y[e]
    return dicionario
print (monta_dicionario(listames, listanumero))