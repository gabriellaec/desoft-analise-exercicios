def subtracao_de_listas(l,s):
    l = [10,7654,32,7,3.1]
    s = [7654,10,32]
    result = l
    i = 0
    for i in l:
    if i in s:
        result.remove(i)
print(result)
