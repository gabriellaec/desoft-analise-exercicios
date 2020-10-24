with open('macacos-me-mordam.txt', 'r') as file:
    content = file.read()
    
words = content.split()
print(words.upper().count("BANANA"))