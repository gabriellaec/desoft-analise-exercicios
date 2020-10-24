with open('churras.txt') as churras:
    total = 0
    for string in churras.read().split('\n'):
        total += int(string.split(',')[1]) + float(string.split(',')[2])

print(total)