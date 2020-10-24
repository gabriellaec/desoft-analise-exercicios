with open ("macacos-me-mordam.txt","r") as arquivo:
    c=0
    for line in arquivo:
        for word in line.split():
           word = word.lower()
           if word == "banana":
               c+=1
print(c)