def bairro_mais_custoso(dic):
    i=0
    for e in dic:
        if dic[e][i]> dic[e][i+1]:
            if dic[e][i]> dic[e][i+2]:
                print (" O bairro com mais gastos é o Bairro 1.")
        elif dic[e][i]< dic[e][i+1]:
            if dic[e][i+1]> dic[e][i+2]:
                print (" O bairro com mais gastos é o Bairro 2 .")
        elif dic[e][i]< dic[e][i+2]:
            if dic[e][i+1]< dic[e][i+2]:
                print (" O bairro com mais gastos é o Bairro 3.")