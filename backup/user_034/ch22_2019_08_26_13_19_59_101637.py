def eh_bissexto(bissex):
    if bissex%4 == 0:
        if bissex%100 != 0:
            return (True)
    else:
        return (False)
        