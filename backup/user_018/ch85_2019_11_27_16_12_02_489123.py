num = 0
with open ('macacos-me-mordam.txt', 'r') as f:
    for line in f:
        for word in line.split():
            if word.lower() == 'banana':
                num +=1
print(num)