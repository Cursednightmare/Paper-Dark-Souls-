import sys
import random
try:
  import replit
  replit.clear()
except Exception:
  pass
#exposition
player_name= ""
Action=""
player_class=""
player_name = input("What is your name?\n >--")
replit.clear()
print(player_name+", The Knight ah yes I have forseen great things from you.")
#we could put the introduction statement here 2/9/20
#player_class = input("Now, how about you pick a class that will make that name great? \n Your choices are \n a Rookie Knight \n or an Worried Mage \n")
class Entities:
  def __init__(self, name, weapon, attacks, health, random_drop):
    self.name = name 
    self.weapon = weapon
    self.attacks = attacks
    self.health = health
    self.random_drop = random_drop

drops_pool=["100 Coins", "Nothing", "Bone", "Nothing", "Health potion", "Nothing"]
misc_items = random.choice(drops_pool)
skeleton = Entities("Skeleton", "sword", 25, 100, misc_items)
#print(skeleton.name, skeleton.health)

class Starting_Class:
  class_name="Knight"
  health=100
  money=300 
class Inventory:
  armor="Armor: Broken Knight Plate"
  weapon="Weapon: Chipped Knight's Blade"
  misc_items="None"
class Room:
  room_name="Starting Room"
class Attacks:
  slash = 25
  hilt_hit = 15
  stab = 20
class Enemy_Attack:
  punch = 15
  kick = 25
  pinch = 10
#Introduction story would be here
print("")
while True:
  print("                               " + Room.room_name)
  print("========================================================================")
  if skeleton.health <= 0:
    print(misc_items)
    print("The " + skeleton.name + " is dead.")
  else:
    print("There's a " +  skeleton.name + " in the room with you and has " + str(skeleton.health) + " health.")
    print("")
  Action=input("Press |A| for attack,\nPress |E| for inventory,\n|S| for character sheet \n|Q| to get moving on your journey. \n ")
  if Action == "A" and skeleton.health > 0:
    Action=input("What attack will you use against the " + skeleton.name +"? \n Press |1| To Slash [25] \n Press |2| For a Hilt Strike [15] \n Press |3| To make a quick stab [20]\n")
    if Action == "1" and skeleton.health > 0:
      replit.clear()
      print("Bop")
      skeleton.health=skeleton.health-50
    elif Action == "2" and skeleton.health > 0:
      replit.clear()
      print("Wham")
      skeleton.health=skeleton.health-15
    elif Action == "3" and skeleton.health > 0:
      replit.clear()
      print("Pow")
      skeleton.health=skeleton.health-20
    else:
      replit.clear()
      print("Wat?")
    print("\n")
  elif Action == "S":
    replit.clear()
    print("Class:"+Starting_Class.class_name)
    print("HP:"+ str(Starting_Class.health))
    print("Money:"+ str(Starting_Class.money))
    print(Inventory.armor)
    print(Inventory.weapon)
    Starting_Class.health = Starting_Class.health-25 
  elif Action == "E":
    replit.clear()
    print(Inventory.armor)
    print(Inventory.weapon)
    print(Inventory.misc_items)
  elif Action == "Q":
    replit.clear()
    print("Alright lets get moving") 
    print("At the end of the room there's a door you enter through that door and enter into the next room.")
  elif Action == 'Quit':
    break
  else:
    if skeleton.health <= 0 and Action =="A":
      replit.clear()
      print("The skeleton is already dead.....")
    else:
      replit.clear()
      print("Wat?")
print("You abandoned the quest")