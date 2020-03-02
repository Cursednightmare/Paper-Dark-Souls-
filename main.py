import sys
import random
import copy
try:
  import replit
  replit.clear()
except Exception:
  pass 
#exposition
class Player:
  def __init__(self, class_name, health, money, armor, weapon, misc_item):
    self.class_name=class_name 
    self.health=health
    self.money=money
    self.armor=armor
    self.weapon=weapon
    self.misc_items=misc_item

classes=[
  Player("Knight", 100, 300, "Broken Knight Plate", "Chipped Knight's Blade", ""), 
  Player("Mage", 80, 300, "Cloth Robe", "Old Stick", "")
]
action=""
player_class=""
player_name = input("What is your name?\n >--")
player_class = input("What class will you be?\n |K| Knight \n |M|Mage \n >--")
if player_class == "K":
  classes[0]
elif action == "M":
  classes[1]
else:
  print("")

replit.clear()
print(player_name + ", The " + Player.class_name + " ah yes I have forseen great things from you.")

#we could put the introduction statement here 2/9/20

class Entity:
  def __init__(self, name, weapon, attacks, health, random_drop):
    self.name = name 
    self.weapon = weapon
    self.attacks = attacks
    self.health = health
    self.random_drop = random_drop

drops_pool=["100 Coins", "Nothing", "Bone", "Nothing", "Health potion", "Nothing"]
misc_items = random.choice(drops_pool)

#enemy = Entity("Skeleton", "Sword", 25, 100, misc_items)
enemies=[Entity("Skeleton", "Sword", 25, 100, misc_items), Entity("Zombie", "Sword", 25, 150, misc_items)]
Entity = random.choice(enemies)


#copy.deepcopy()

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
  
  if Entity.health <= 0:
    print(misc_items)
    print("The " + Entity.name + " is dead.")
  else:
    print("There's a " +  Entity.name + " in the room with you and has " + str(Entity.health) + " health.")
    print("")
  action=input("Press |A| for attack,\nPress |E| for inventory,\n|S| for character sheet \n|Q| to get moving on your journey. \n ")
  if action == "A" and Entity.health > 0:
    action=input("What attack will you use against the " + Entity.name +"? \n Press |1| To Slash [25] \n Press |2| For a Hilt Strike [15] \n Press |3| To make a quick stab [20]\n")
    if action == "1":
      replit.clear()
      print("Bop")
      Entity.health=Entity.health-50
    elif action == "2":
      replit.clear()
      print("Wham")
      Entity.health=Entity.health-15
    elif action == "3":
      replit.clear()
      print("Pow")
      Entity.health=Entity.health-20
    else:
      replit.clear()
      print("Wat?")
    print("\n")
  elif action == "S":
    replit.clear()
    print("Class:"+knight.class_name)
    print("HP:"+ str(knight.health))
    print("Money:"+ str(knight.money))
    print(knight.armor)
    print(knight.weapon)
    knight.health = knight.health-25 
  elif action == "E":
    replit.clear()
    print(knight.armor)
    print(knight.weapon)
    print(knight.misc_items)
  elif action == "Q":
    replit.clear()
    print("Alright lets get moving") 
    print("At the end of the room there's a door you enter through that door and enter into the next room.")
  elif action == 'Quit':
    break
  else:
    if Entity.health <= 0 and action =="A":
      replit.clear()
      print("The " + Entity.name + " is already dead.....")
    else:
      replit.clear()
      print("Wat?")
print("You abandoned the quest")