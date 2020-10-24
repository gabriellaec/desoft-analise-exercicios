from collections import Counter
with open("texto.txt", "r") as file:
    w=file.readlines()
x=",".join(w)

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

print(word_count(x))
