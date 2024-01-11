print("⚔️ BATTLE SCENARIO ⚔️")
import os, time, random

def health():
  six_sided_dice = random.randint(1, 6)
  twelve_sided_dice = random.randint(1, 12)
  health_stat = ((six_sided_dice * twelve_sided_dice) / 2) + 10
  return health_stat


def strength():
  six_sided_dice = random.randint(1, 6)
  eight_sided_dice = random.randint(1, 8)
  strength_stat = ((six_sided_dice * eight_sided_dice) / 2) + 12
  return strength_stat

print("⚔️ BATTLE TIME ⚔️")
print()
c1Name = input("Name your Legend:\n")
Type1 = [
  'human', 'imp', 'wizard', 'elf', 'dwarf', 'gnome', 'orc', 'goblin',
  'dwarf', 'halfling'
]
c1Type = random.choice(Type1).upper()
print()
print(c1Name,"\n",c1Type)
c1Health = health()
c1Strength = strength()
print("HEALTH:", c1Health)
print("STRENGTH:", c1Strength)
print()
print("Who are they battling?")
print()
c2Name = input("Name your Legend:\n")
Type2 = [
  'human', 'imp', 'wizard', 'elf', 'dwarf', 'gnome', 'orc', 'goblin',
  'dwarf', 'halfling'
]
c2Type = random.choice(Type2).upper()
print()
print(c2Name,"\n",c2Type)
c2Health = health()
c2Strength = strength()
print("HEALTH:", c2Health)
print("STRENGTH:", c2Strength)
print()

round = 1
winner = None


while True:
  time.sleep(2)
  os.system("clear")
  print("⚔️ BATTLE TIME ⚔️")
  print()
  print("The battle begins!")
  c1Dice = strength()
  c2Dice = strength()

  difference = abs(c1Strength - c2Strength) + 1

  if c1Dice > c2Dice:
    c2Health -= difference
    if round==1:
      print(c1Name,'the',c1Type, "wins the first blow")
    else:
      print(c1Name,'the',c1Type, "wins round", round)
  elif c2Dice > c1Dice:
    c1Health -= difference
    if round==1:
      print(c2Name,'the',c2Type, "wins the first blow")
    else:
      print(c2Name,'the',c2Type, "wins round", round)
  else:
    print("Their swords clash and they draw round", round)
    
  print()
  print(c1Name,'the',c1Type)
  print("HEALTH:", c1Health)
  print()
  print(c2Name,'the',c2Type)
  print("HEALTH:", c2Health)
  print()
  
  if c1Health<=0:
    print(c1Name,'the',c1Type, "has died!")
    winner = c2Name
    break
  elif c2Health<=0:
    print(c2Name,'the',c2Type, "has died!")
    winner = c1Name
    break
  else:
    print("And they're both standing for the next round")
    round += 1
    
time.sleep(1)
os.system("clear")
print("⚔️ BATTLE TIME ⚔️")
print()
print('\033[31;1;4m',winner,'\033[0m' "has won in",'\033[1;35m', round, '\033[0m',"rounds")

