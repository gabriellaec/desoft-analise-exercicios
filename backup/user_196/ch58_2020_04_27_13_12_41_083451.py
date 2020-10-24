qnt = 0
def conta_a(str):
    for i in str:
        if str[i] == "a":
            qnt +=1
        else:
            break
    return qnt        
    