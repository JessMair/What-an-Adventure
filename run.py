# Intro for the player 

print("You have opened the doors of the unknown")

# Player prompted to enter name to begin playing. 

name = input("Enter your name to play: ").capitalize().strip()
print ("Hello", name, "you have now entered the world of Adventure!!")

# Main section of the game. The player is asked a question at a time with 2 options to choose from

question_one = input("You open your eyes to find that you can see snow miles on end. A polar bear appears charging at you some 50 meters away. You have 2 options, start running or lay on the ground and play dead. Type run or dead: ").lower().strip()

if answer == "run" :
    print("Did you really think you could out run a polar bear? The bear caught you!! Game over")
    

elif answer == "dead" :
    question_two = input("")

else:
    print("That is an incorrect response. Game Over.")
    