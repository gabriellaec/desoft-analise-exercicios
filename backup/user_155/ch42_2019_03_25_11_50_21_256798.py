def quantos_uns(string):
    i = 0
    uns = 0 
    while i < len(string):
        if string[i] == '1':
            uns +=1
        i+=1
    return uns
string = str(107394198471298761293468120349106230461290467812649712046129)
print(quantos_uns(string))
