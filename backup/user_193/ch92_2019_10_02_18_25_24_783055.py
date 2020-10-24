def simplifica_dict(d):
    abc=["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
    l=[]
    for x in d.values():
        l.append (x)
    for x in d.keys():
        l.append (x)
    return l

print (simplifica_dict({'a': 'b', 'c': 'b', 'b': 'a'}))