x = 2
i = 0
k = 1
recorde_atual = 0
while x < 1000:
    i = 0
    while x != 1:
        if x%2 == 0:
            x = x/2
            i += 1
        else:
            x = (3*x + 1)/2
            i += 2
        print(x)
    if i > recorde_atual:
        recorde_atual = i
    k += 1
    x += k
print(recorde_atual)