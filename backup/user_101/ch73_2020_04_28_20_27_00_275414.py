def remove_vogais(s):
    v = ['a','e','i','o','u']
    f = ''
    for e in s:
        print(e)
        if e in v:
            f += e
    return f
print(remove_vogais('aeiou'))
