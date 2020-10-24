def nome_usuario(digite):
    a = '@'
    new = []
    for i in range(len(digite)):
        if a == digite[i]:
            while i >= 0:
                new.append(digite[i])
                i -= 1               
            return new
            