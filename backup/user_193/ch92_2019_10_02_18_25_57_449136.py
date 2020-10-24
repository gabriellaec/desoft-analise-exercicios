def simplifica_dict(d):
    l=[]
    for x in d.values():
        l.append (x)
    for x in d.keys():
        l.append (x)
    return l