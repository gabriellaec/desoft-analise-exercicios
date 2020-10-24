def primos_entre(x,y):
    x = int(x)
    y = int(y)
    var = x
    lista = []
    while var <= y:
        if eh_primo(var):
            lista.append(var)
            var = var + 1
            numb = numb + 1
        else:
            var = var + 1
    return lista