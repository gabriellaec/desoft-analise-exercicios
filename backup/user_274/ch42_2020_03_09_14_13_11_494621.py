list = []
word=input("Escreva uma palavra. ")
list.append(word)

while word != "fim":
    word=input("Escreva uma palavra. ")
    list.append(word)
n=len(list)

while i < n:
    if list[i][1] == "a":
        print(list[i])
    i=i+1
