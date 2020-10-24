words = []

for i in range(0, 5):
    words.append(input("Palavra?"))

print("fim")

for word in words:
    if word[0] == "a":
        print(word)
