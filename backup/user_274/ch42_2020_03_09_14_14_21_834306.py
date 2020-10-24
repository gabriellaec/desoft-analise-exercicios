list = []
word=input("Escreva uma palavra. ")
list.append(word)

while word != "fim":
    word=input("Escreva uma palavra. ")
    list.append(word)
n=len(list)
i=0

while i < n:
    if list[i][0] == "a":
        print(list[i])
    i=i+1
