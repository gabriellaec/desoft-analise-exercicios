def pos_arroba(email):
    i=0
    ON = True
    while ON:
        if email[i]=="@":
            ON=False
        i+=1
    return i