file=open("macacos-me-mordam.txt","r")
wordcount=0
for word in file.read().split():
    if "banana" in word:
        wordcount+=1
print(wordcount)
file.close();