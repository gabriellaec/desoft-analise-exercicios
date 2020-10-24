def quantos_uns(string):
    i = 0
    uns = 0 
    while i < len(string):
        if string[i] == '1':
            uns +=1
        i+=1
    return uns
string = str(input('Digite um número: '))
print(quantos_uns(string))
