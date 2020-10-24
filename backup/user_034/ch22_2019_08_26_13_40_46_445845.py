def eh_bissexto(bissex):
    if bissex%4 == 0:
        return(True)
    else:
        if bissex%100 != 0:
            if bissex%400 == 0:
                return (True)
            else:
                return (False)
        else:
        	return (False)