from math import sin, pi

target_distance = 100

angle = float(input()) / 180 * pi
speed = float(input())

contact_distance = speed ** 2 * sin(2 * angle) / 9.8

if contact_distance > target_distance + 2: print('Muito longe')
elif contact_distance < target_distance - 2: print('Muito perto')
else: print('Acertou!')