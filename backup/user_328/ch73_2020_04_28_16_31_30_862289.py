def remove_vogais(string):
    v= ['a','e','i','o','u']
    l= []
    for i in string:
        l.append(i)
        for x in v:
            if i == x:
                l.remove(i)
    return (''.join(l))