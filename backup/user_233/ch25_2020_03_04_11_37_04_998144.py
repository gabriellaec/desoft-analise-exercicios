from math import sin

target_distance = 100

angle = float(input())
speed = float(input())

contact_distance = v ** 2 * sin(2 * angle) / 9.8

if contact_distance > target_distance + 2: print('Muito longe')
elif contact_distance < target_distance - 2: print('Muito perto')
else: print('Acertou!')