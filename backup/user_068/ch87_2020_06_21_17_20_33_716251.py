with open('churras.txt', 'r') as arquivo:
    b = arquivo.read
    c = b.split()
    i = 1
    while i < len(c):
        
        despesa = c[i]*c[i+1]
        print(despesa)