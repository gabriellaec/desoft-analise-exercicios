def pos_arroba(email):
    for p,i in enumerate(email):
        if i == '@':    
            return p
print(pos_arroba('gabicuki@gmail.com'))