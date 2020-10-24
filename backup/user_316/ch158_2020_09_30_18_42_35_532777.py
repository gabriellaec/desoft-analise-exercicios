with open('texto.txt', r) as file:
    content = file.read()
    
words = content.split()
print(len(words))