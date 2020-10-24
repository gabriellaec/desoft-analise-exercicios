import random

moneys = 100

def is_odd (number):
    return bool(number % 2)

while moneys > 0:
    print(moneys)
    
    bid = int(input("Aposta? "))
    bet = None

    if bid == 0:
        break
              
    bet_type = input("Número ou padrade? (n/p) ")
              
    if bet_type == "n":
        bet = int(input("Número? "))
                 
    elif bet_type == "p":
        bet = input("Par ou Ímpar? (p/i) ")
                 
    else:
        continue
                 
    match = random.randint(0, 36)
                 
    if bet_type == "n" and bet == match:
        bid *= 35
    elif bet_type == "p":
        if is_odd(match) and bet != "i" or not is_odd(match) and bet != "p":
          bid *= -1
    else:
        bid *= -1

    moneys += bid
    
print(moneys)
