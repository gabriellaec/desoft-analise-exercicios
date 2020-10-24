def pos_arroba(email):
    i = 0
    while i <len(email):
        if email[i] == '@':
            a = i
            i+=1
        else:
            i+=1
            
    return a

def nome_usuario(x):
    return x[ :a]