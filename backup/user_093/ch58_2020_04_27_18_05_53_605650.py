x='aaaa'
def conta_a(x):
    i=0
    p=0
    while i < len(x):
        if x[i]=='a':
            p+=1
            
        i+=1
    return p

print(conta_a(x))