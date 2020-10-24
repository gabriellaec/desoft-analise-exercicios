with open('macacos-me-mordam.txt', 'r') as file:
    content = file.read()
    
print(content.upper().count("BANANA"))