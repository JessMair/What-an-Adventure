# To allow time delay in game 
import time

# Upper and lower case that the player may use 
answer_A = ["A", "a"]
answer_B = ["B", "b"]

#To reduce duplication of code 
required = ("\nUse only A or B\n")

#Intro the player 
print("""You have opened the doors of the unknown""")

def get_name():
    """ Player prompted to enter name to begin playing. """
    name = input("Enter your name to play: ").capitalize().strip()
    if name != '':
      print ("Hello", name, "you have now entered the world of Adventure!!")
    else:
        print ("""you must enter a name to play""")
        get_name()

def get_response():
  """Player promted to enter A or B"""
  print("Please enter A or B")
  choice = input(">>> ")
  
def game():
    """ Main section of the game. The player is asked a question at a time with
    2 options to choose from
    """
# Question 1    
    print ("You open your eyes to find that you can see snow miles on end.\
      A polar bear appears charging at you some 50 meters away.")
     
time.sleep(2)

print (""" You have 2 options, start running or lay on the ground and play dead.
  Type: 
  A. Run 
  B. Play dead """)
choice = input(">>> ") 

# Below are the consequences of the answers to question 1
if answer is A: 
  print("Did you really think you could out run a polar bear?\
          The bear got you!! Game over")

elif answer is B: 
  # Question 2
  print ("""That was a clever move. The coast is now clear, 
  you start walking and 5 minutes later you come accross a 
  paddle boat and a sleigh. """)
  
  time.sleep(3)
            
  print("""Pick one to continue your journey. 
  Type: 
  A. Paddle 
  B. Sleigh """)
  choice = input(">>> ")

  else: print ("Incorrect response")
  get_response()

  # Below are the consequences of the answers to question 2 
  if answer is A: 
  # Question 3
  print(""""That turned out to be a wise choice because you soon
          come across a river and use your boat to get across. Now on the other side you
          find a jungle, deep in this jungle you bump into a tiger. Do you climb a tree or
          approach the tiger to reassure him that you are friendly?""")

  time.sleep(2)

  print("""Type:
  A. To climb 
  B. To approach """)
  choice = input(">>> ")

  elif answer is B:
    print ("Ummm, there are no hounds to pull the sleigh. Game over !!")

  else: print ("Incorrect response")
  get_response()
  
# Below are the consequences to the answers to question 3
if answer is A:
# Question 4
  print(""""Well done, getting high up is the smart
    thing to do. The coast looks clear but you can not be too 100% certain. 
    Do you take a nap until it gets dark or do you climb 
    down to continue your journey?""")

  time.sleep(2)

  print("""Type:
  A. To nap 
  B. To climb down """)
  choice = input(">>> ")

  elif answer is B: 
    print("uh-oh! Not the wisest decision, the tiger is not pleased. Game Over !!")

  else: print ("Incorrect response")
  get_response()
  
# Below are the consequences to the answers to question 4
if answer is A:
  print("Oh dear, you fell off whilst sleeping. Game over!!")

elif answer is B: 
  #Question 5
  print("""You make your way through the jungle 
  and come upon a treasure chest with a key""")

  time.sleep(2)

  print("""Do you open it or keep walking? 
  Type 
  A. To open it 
  B. To keep walking """)
  choice = input(">>> ")

else: print ("Incorrect response")
get_response()

# Below are the consequences to the answers to question 5
if answer is A: 
  print("Uh-oh, you have unleashed a king cobra aarggghhhh!! Game over!!")

elif answer is B:
  # Question 6
  print("You followed your instincts and kept the lid on the treasure box. ")


else: print ("Incorrect response")
get_response()

# Below are the consequences to the answers to question 6


            
              



get_name()
game()
get_response()