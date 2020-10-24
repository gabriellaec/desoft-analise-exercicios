max_termos=0
max_num=0
for n in range(2, 1000):
    num=n
    termos=0
    while num>1:
        if num%2 == 0:
            num/=2
        else:
            num=num*3+1
        termos+=1
    if termos>max_termos:
        max_termos=termos
        max_num=n
print("A maior sequência se obtém com o número {0} com {1} termos".format(max_num, max_termos))