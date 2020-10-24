def junta_nome_sobrenome(a, b):
    listans = []
    i = 0
    
    while i < len(a):
        listans.append('{0}{1}'.format(a[i]+b[i]))
        i += 1
    return listans    
a = ['enrico', 'rafael', 'silvana']
b = [ 'costa',  'nadal',  'venturini']
print(junta_nome_sobrenome
