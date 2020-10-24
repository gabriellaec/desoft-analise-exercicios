def eh_bissexto(bissex):
    if bissex%400 == 0:
        return(True)
    else:
        if bissex%100 == 0:
            return(False)
    if bissex%4 == 0:
        return (True)
    else:
        return (False)
        