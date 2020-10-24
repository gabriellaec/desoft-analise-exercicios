lista = ['caio','amanda','gabi','felps','deco','gabes','noia']
def alunos_impares(lista):
    saida = []
    i=1
    while i < len(lista):
        impares = lista[i]
        saida.append(impares)
        i += 2
    return saida
