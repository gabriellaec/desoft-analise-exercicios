words = []

while True:
    word = input("Palavra?")
    
    if word == "fim":
        break
    else:
        words.append(word)

for word in words:
    if word[0] == "a":
        print(word)
