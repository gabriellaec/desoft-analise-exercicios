moneys = 100

def is_odd (number):
    return bool(number % 2)

while money > 0:
    print(money)
    
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
                 
    if bid_type == "n" and bet == match:
        bid *= 35
    elif is_odd(match) and bet == "i" or not is_odd(match) and bet == "p":
         # does notting :)
    else:
        bid *= -1

    money += bid
    
print(money)
