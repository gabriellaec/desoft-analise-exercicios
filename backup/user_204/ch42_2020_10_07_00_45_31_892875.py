word = 0
while word != "fim":
    word = input("Qual a palavra? ")
    if word[0] == "a":
        with_a = []
        with_a.append(word)
print(with_a)