file=open("macacos-me-mordam.txt","r")
wordcount=0
for word in file.read():
    if "banana"or"BANANA" or "BaNaNa" == word:
        wordcount+=1
print(wordcount)
file.close();