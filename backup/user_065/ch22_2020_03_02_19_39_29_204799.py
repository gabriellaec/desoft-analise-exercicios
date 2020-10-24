ciggys = int(input("How manny ciggys per day m8?"))
years = int(input("How manny years you smoke cunt?"))
yearsLost = 0
for d in range(years):
    yearsLost = ciggys * 365

yearsLost = yearsLost / 1440

print("you lost {0: .0f} days dude".format(yearsLost))