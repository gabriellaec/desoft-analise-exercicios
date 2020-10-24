word = 0
while word != "fim":
    word = input("Qual a palavra? ")
    if word[0] == "a":
        with_a = []
        with_a.append(word)

i = 0
while i < len(with_a):
    print(with_a[i])
    i += 1