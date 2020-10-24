def verifica_progressao(lista):
    for numero in range(len(lista)):
        if lista[numero] + lista [numero + 1] == lista[numero + 1] + lista[numero + 2]:
            if lista[numero] / lista [numero + 1] == lista[numero + 1] / lista[numero + 2]:
                return "AG"
            else:
                return "PA"
        elif lista[numero] / lista [numero + 1] == lista[numero + 1] / lista[numero + 2]:
            return "PG"
        else:
            return "NA"