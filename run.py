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

if answer is A: 
  print("Did you really think you could out run a polar bear?\
          The bear got you!! Game over")

elif answer is B: 
  print ("""That was a clever move.\
          The coast is now clear, you start walking and 5 minutes later you\
            come accross a paddle boat and a sleigh.Pick one to continue\
              your journey. 
              Type: 
              A. Paddle 
              B. Sleigh """)
  choice = input(">>> ")

  #else : print ("Incorrect response")
  get_response()



            
              







get_name()
game()
get_response()