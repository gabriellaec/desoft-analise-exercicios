def traduz(lista, dic):
    traducao = []
    for word in lista: 
        palavra= dic[word]
        traducao.append(palavra)
       
    return traducao