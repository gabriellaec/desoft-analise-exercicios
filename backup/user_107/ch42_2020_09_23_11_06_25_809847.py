words = []

for i in range(0, 5):
    word = input("Palavra?")
    
    if word:
        words.append(word)

print("fim")

for word in words:
    if word[0] == "a":
        print(word)
