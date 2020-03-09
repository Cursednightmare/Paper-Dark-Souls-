import sys
import random
import copy
try:
  import replit
  replit.clear()
except Exception:
  pass 

#exposition


class Room:
  def __init__(self, name, enemy, rnd_loot,):
    self.name=name
    self.enemy=enemy  
    self.rnd_loot=rnd_loot 

class Attack:
  def __init__(self, name, damage):
    self.name = name  
    self.damage = damage 

class Player:
  def __init__(self, class_name, health, money, armor, weapon, misc_items, attacks):
    self.class_name=class_name 
    self.health=health
    self.money=money
    self.armor=armor
    self.weapon=weapon
    self.misc_items=[]
    self.attacks=attacks


classes=[
  Player("Knight", 100, 300, "Broken Knight Plate", "Chipped Knight's Blade", "",[Attack("Slash", 50)]),
  Player("Mage", 80, 300, "Cloth Robe", "Old Stick", "", [Attack("Boop", 50)])
]

class Enemy:
  def __init__(self, name, weapon, attacks, health, random_drop):
    self.name = name 
    self.weapon = weapon
    self.attacks = attacks
    self.health = health
    self.random_drop = random_drop
    
drops_pool=["100 Coins", "Nothing", "Bone", "Nothing", "Health potion", "Nothing"]
misc_items=random.choice(drops_pool)



enemies=[Enemy("Skeleton", "Sword", [Attack("Stab", 20), Attack("Slap", 25)], 100, misc_items), 
Enemy("Zombie", "Sword", [Attack("Hit", 15)], 150, misc_items)
]

enemy = random.choice(enemies)

player_name = input("What is your name?\n >--")
while True:
  player_class = input("What class will you be?\n |K| Knight \n |M|Mage \n >--")
  if player_class == "K":
    player=classes[0]
    break
  elif player_class == "M":
    player=classes[1]
    break
  else:
    print("Wat")


replit.clear()
print(player_name + ", The " + player.class_name + " ah yes I have forseen great things from you.")

#we could put the introduction statement here 2/9/20

#copy.deepcopy()

#Introduction story would be here
Room.name = "Starting Room"
print("")
while True:
  print("                               " + Room.name)
  print("===========================================================================")
  
  if enemy.health <= 0:
    print("The enemy dropped: " + misc_items)
    print("The " + enemy.name + " is dead.")
  else:
    print("There's a " +  enemy.name + " in the room with you and has " + str(enemy.health) + " health.")
    print("")
  action=input("Press |A| for attack,\nPress |E| for misc_items,\n|S| for character sheet \n|Q| to get moving on your journey. \n|P| to pick up items on the ground \n>--")
  if action == "A" and enemy.health > 0:
    action=input("What attack will you use against the " + enemy.name +"? \n Press |1| To Slash [25] \n Press |2| For a Hilt Strike [15] \n Press |3| To make a quick stab [20]\n")
    if action == "1":
      replit.clear()
      print("Bop")
      enemy.health=enemy.health-50
    elif action == "2":
      replit.clear()
      print("Wham")
      enemy.health=enemy.health-15
    elif action == "3":
      replit.clear()
      print("Pow")
      enemy.health=enemy.health-20
    else:
      replit.clear()
      print("Wat?")
    print("\n")
  elif action == "S":
    replit.clear()
    print("Class:" + player.class_name)
    print("HP:"+ str(player.health))
    print("Money:"+ str(player.money))
    print(player.armor)
    print(player.weapon)
    player.health = player.health-25 
  elif action == "E":
    replit.clear()
    print(player.armor)
    print(player.weapon)
    print(player.misc_items)
  elif action == "Q":
    replit.clear()
    print("Alright lets get moving") 
    print("At the end of the room there's a door you enter through that door and enter into the next room.")
  elif action == "P":
    replit.clear()
    print("You have picked up the following")
    #IDK 
  elif action == 'Quit':
    break
  else:
    if enemy.health <= 0 and action =="A":
      replit.clear()
      print("The " + enemy.name + " is already dead.....")
    else:
      replit.clear()
      print("Wat?")
print("You abandoned the quest")