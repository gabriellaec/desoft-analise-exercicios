
def pos_arroba(str):
    for p in range(len(str)):
        if str[p]=="@":
            return p
     
def nome_usuario(email):

    arroba = pos_arroba(email)
    
    return email[:arroba]

teste="jao@hotmail.com"
print(nome_usuario(teste)) 