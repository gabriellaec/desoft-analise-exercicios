def remove_vogais(s):
    v = ['a','e','i','o','u']
    for e in s:
        if e in v:
            s.replace(e,'')
    return s