
def soma_valores(my_list):
    s = 0
    i = 0
    while i < len(my_list):
        s += my_list[i]
        i += 1
    return s
print(soma_valores([2,5,3]))
    