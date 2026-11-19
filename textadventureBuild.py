#Creating the player
player = {"name": "defaultname", "age": "defaultage", "level": 1}
#Creating the inventory (it is empty at first)
inventory = []

#answer2 isn't defined. How???
 
#Left room
def left():
  print("You have entered the hallway")
  print("You found a coin")
  #How to add to a list
  inventory.append("coin")

  #Loop through a list to find an item
  for x in inventory:
    if x == "coin":
      print("You have a coin in your pocket")

  print("You immediately lost it")
  #How to remove from a list
  inventory.remove("coin")

#Right room
def right():
  print("You have entered the kitchen")
  #Edit a key value in a dictionary (like our name)



  #Straight room
def straight():
  print("You have survived the traps") #edit all...
  #Edit a key value in a dictionary (like our name)
        #...of this.
#Left room (2nd set)
def leftTwo():
  print("You find Mei, aptly named 'The Cold Day in Hell' and begin to battle her.")
  print("You are beaten and then promptly frozen to death. :)")
  print("GAME OVER.")
  return False  # Tells main() that the player died
  #How to add to a list
  inventory.append("styk")

  #Loop through a list to find an item
  for x in inventory:
    if x == "styk":
      print("You are dead, I'm afraid.")

  print("The styk only confirms that you must join the other lost souls.")
  #How to remove from a list
  inventory.remove("styk")

#Right room (2nd set)
def rightTwo():
  print("Nothing is down this way...except a key...")
  print("...you get so happy that it falls down your esophagus and you die")
  #Edit a key value in a dictionary (like our name)
  return False  # Tells main() that the player died


  #Straight room (2nd set)
def straightTwo():
  print("You have won. Triumph.") 
  #Edit a key value in a dictionary (like our name)
  return True  # Tells main() that the player survived

#Main function
def main():
  answer =  player["name"] = input("What is your name btw? ")
  print("Hello", player["name"])
  answer = input("Where do you want to go?\nEnter 'left' , 'right' , or 'straight'")
  #Make sure to convert our answers to lowercase
  answer = answer.lower()

  #Match case (alternative to an if/else statement)
  match answer:
    case "left":
      print("To the left! To the left")
      left()
    case "right":
      print("Right choice?")
      right()
    case "straight":
      print("Okay we are going rig- I mean straight")
      straight()
    case _:
      print("LEFT OR RIGHT.")
      main()
      return
  answer2 = input("Where to now?\nEnter 'left' , 'right' , or 'straight'")
        #Make sure to convert our answers to lowercase
  answer2 = answer2.lower()
      
        
    
  #second set before Win. EDIT ACCORDINGLY
  match answer2:
    case "left":
          print("To the left! To the left")
          leftTwo()
    case "right":
          print("Right way this time")
          rightTwo()
    case "straight":
          print("Are you ready for this?")
          straightTwo()
    case _:
      print("Time is running out. Choose a path, or I will kill you myself.")
      #Call the function within the function (restart, recursion)
      main()
      return

#Add this to make the main function run by default
if __name__ == "__main__":
  main()