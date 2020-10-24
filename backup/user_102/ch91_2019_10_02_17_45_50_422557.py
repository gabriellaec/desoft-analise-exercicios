file = open("palavras.txt", "r")
wordcount = 0
line = file.readlines()
for lines in line:
    words = lines.split()
    for word in words:
        if word[:1] == "a" or "A":
            wordcount += 1
print(wordcount)
file.close()
