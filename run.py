import time

# Upper and lower case that the player may use 
answer_A = ["A", "a"]
answer_B = ["B", "b"]

#To reduce duplication of code 
required = ("\nUse only A or B\n")
#Intro the player 
print("You have opened the doors of the unknown")

def get_name():
    """ Player prompted to enter name to begin playing. """
    name = input("Enter your name to play: ").capitalize().strip()
    if name != '':
        print ("Hello", name, "you have now entered the world of Adventure!!")
    else:
        print ("you must enter a name to play")
        get_name()

def game():
    """ Main section of the game. The player is asked a question at a time with
    2 options to choose from
    """
    print ("You open your eyes to find that you can see snow miles on end.\
      A polar bear appears charging at you some 50 meters away.")
     
time.sleep(2)

print (""" You have 2 options, start running or lay on the ground and play dead.
  Type: 
  A. Run 
  B. Play dead """)
choice = input(">>> ") 



get_name()
game()