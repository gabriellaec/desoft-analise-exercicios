def nome_usuario(digite):
    a = '@'
    new = []
    for i in range(len(digite)):
        if a == digite[i]:
            while i > 0:
                i -= 1
                new.append(digite[i])               
    t = new[::-1]  
    return ''.join(t)
            