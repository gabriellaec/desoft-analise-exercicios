i = 0
list = []
ls = []
a = True
num = int(input("Insira seu numero"))
while a:
    if num <= 0:
        a = False
    else:
            list.append(num)
            num = int(input("Insira seu numero"))
while i < len(list):
    ls.append(-i)
    i = i + 1
print(ls)

