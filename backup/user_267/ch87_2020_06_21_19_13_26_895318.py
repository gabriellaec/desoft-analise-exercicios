with ('churras.txt','r') open as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        total += linha[1]*linha[2]
    return total
    