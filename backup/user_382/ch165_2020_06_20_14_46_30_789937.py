def mais_populoso(dic):
    maximo = 0 
    for i in dic:
        for t in dic[i].values():
            if t > maximo:
                maximo = t
    return print(maximo) 

            