p = input('Qual a palavra? ')
a = []
while p != "fim":
    a.append(p)
    p = input('Qual a palavra? ')
    
i = 0
while i < len(a):
    if a[i][0]== "a":
        print(a[i])
    i += 1
    