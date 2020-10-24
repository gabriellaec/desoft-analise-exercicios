with open('macacos-me-mordam.txt', 'r') as arq:
    cont = arq.read()
word = cont.lower().split()
i = 0
for t in word:
    if "banana" == t :
        i+=1
print(i)