def conta_a(palavra):
    i = 0
    s = 0
    while i <len(palavra):
        if 'a' == palavra[i]:
            s+=1
        i+=1
    return s
palavra1 = input("Digite uma palavra:")
print(conta_a(palavra1))