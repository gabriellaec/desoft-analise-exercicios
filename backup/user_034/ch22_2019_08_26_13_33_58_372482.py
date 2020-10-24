def eh_bissexto(bissex):
    if bissex%4 == 0:
        if bissex%100 != 0:
            if bissex%400 == 0:
                return (True)
            else:
                return (False)
        else:
        	return (True)
    else:
        return (False)
        