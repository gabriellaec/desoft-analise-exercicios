num = int(input("Escolha números"))
a = 0
while num != 0:
    a = a + num
    num = int(input("Escolha números"))
if num == 0:
    print(a)
    