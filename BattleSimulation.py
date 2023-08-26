#EXAMPLE OF WHAT IT SHOULD LOOK LIKE

#⚔️ BATTLE TIME ⚔️

#Name your Legend:
#Character Type (Human, Elf, Wizard, Orc): 
#Elf

#Arthur the Magnificent
#HEALTH: 13
#STRENGTH: 18

#Who are they battling?

#Name your Legend:
#Sheila the Almighty
#Character Type (Human, Elf, Wizard, Orc): 
#Human

#Sheila the Almighty
#HEALTH: 40
#STRENGTH: 26

#*clear screen here*

#⚔️ BATTLE TIME ⚔️

#The battle begins!

#Arthur wins the first blow
#Sheila takes a hit, with 8 damage

#Arthur the Magnificent
#HEALTH: 13

#Sheila the Almighty
#HEALTH: 32

#And they're both standing for the next round!

#*clear screen here*

#⚔️ BATTLE TIME ⚔️

#The battle continues!

#Sheila wins round 2
#Arthur takes a hit, with 8 damage

#Arthur the Magnificent
#HEALTH: 5

#Sheila the Almighty
#HEALTH: 32

#And they're both standing for the next round!

#*clear screen here*

#⚔️ BATTLE TIME ⚔️

#The battle continues!

#Sheila wins round 3
#Arthur takes a hit, with 8 damage

#Arthur the Magnificent
#HEALTH: -3

#Sheila the Almighty
#HEALTH: 32

#Oh no Arthur the Mighty has died!

#Sheila the Almighty destroyed Arthur the Magnificent in 3 rounds!
#Ex on how the final layout should be close too

import random
import os
import time

def diceRoll(side):
  result = random.randint(1,side)
  return result

def health():
  hp = ((diceRoll(6)*diceRoll(12))/2)+10
  return hp

def strength():
  st = ((diceRoll(6)*diceRoll(8))/2)+12
  return st


print("⚔️ BATTLE ⚔️")
print()
heroName = input("Name your Hero: ")
print()
heroType = input("what is your Character Type (Human, Elf, Mage, Witch, Orc): ")
print()
print(heroName)
heroHp = health()
heroSt = strength()
print("HEALTH:", heroHp)
print("STRENGTH:", heroSt)
print()
print("Who are they Battling? ")
print()

oppName = input("Your Oppenent: ")
print()
oppType = input("what is your Oppenent Type (Human, Elf, Mage, Witch, Orc): ")
print()
print(oppName)
oppHp = health()
oppSt = strength()
print("Health:", oppHp)
print("Strength:", oppSt)
print() 

round = 1
winner = None

while True:
  time.sleep(1)
  os.system("clear")
  print("⚔️ BATTLE TIME ⚔️")
  print()
  print("The battle begins...")

  heroDice = diceRoll(6)
  oppDice = diceRoll(6)

  difference = abs(heroSt - oppSt) + 1

  if heroDice > oppDice:
    oppHp -= difference
    if round == 1:
      print(heroName, "wins in one strike!")
    else:
      print(heroName, "Wins round", round)
  elif oppDice > heroDice:
    heroHp -= difference
    if round == 1:
      print(oppName,"wins in one strike!")
    else:
      print(oppName,"wins round", round)
  else:
    print("Their swords clash and they draw round", round)

  print()
  print(heroName)
  print("Health:", heroHp)
  print()
  print(oppName)
  print("Health:", oppHp)
  print()

  if heroHp <= 0:
    print(heroName,"has died!")
    winner = oppName
    break
  elif oppHp <= 0:
    print(oppName, "has died!")
    winner = heroName
    break
  else:
    print("And they are both still standing for the next round")
    round += 1

time.sleep(1)
os.system("clear")
print("⚔️ BATTLE TIME ⚔️")
print()
print(winner, "has won in", round ,"rounds!")