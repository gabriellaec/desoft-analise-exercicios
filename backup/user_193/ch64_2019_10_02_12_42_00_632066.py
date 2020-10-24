def nome_usuario(x):
    i=0
    while x[i]!="@":
        i+=1
    return x[:i]