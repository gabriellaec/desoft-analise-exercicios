with open('cancao_do_exilio.txt', 'r') as arquivo:
    x = arquivo.read().lower()
    a = x.split()
    n = 0
    for i in a:
        if i == 'banana':
            n+=1
print(n)
