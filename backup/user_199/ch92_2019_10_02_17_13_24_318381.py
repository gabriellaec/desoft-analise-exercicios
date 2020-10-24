dic={'abacate':'abacate'}

def simplifica_dict(dic):
    l=[]
    for k,v in dic.items():
        if k not in l:
            l.append(k)
    return l
print(simplifica_dict(dic))