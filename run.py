# Intro for the player 

print("You have opened the doors of the unknown")

# Player prompted to enter name to begin playing. 

name = input("Enter your name to play: ").capitalize().strip()
print ("Hello", name, "you have now entered the world of Adventure!!")

# Main section of the game. The player is asked a question at a time with 2 options to choose from

question_one = input("You open your eyes to find that you can see snow miles on end. A polar bear appears charging at you some 50 meters away. You have 2 options, start running or lay on the ground and play dead. Type run or dead: ").lower().strip()

if answer == "run" :
    print("Did you really think you could out run a polar bear? The bear got you!! Game over")
    

#elif answer == "dead" :
    #question_two = input("That was a clever move. The coast is now clear, you start walking and 5 minutes lateryou come accross a paddle boat and a sleight. Pick one to continue your journey. Type paddle or sleigh: ").lower().strip()

    #if answer =="paddle" : 
        #question_three = input("That turned out to be a wise choice because you soon come across a river and use your boat to get across. Now on the other side you find a jungle, deep in this jungle you bump into a tiger. Do you climb a tree or approach the tiger to reassure him that you are friendly? Type climb or approach").lower().strip()

       # if answer == "tree" :
    #        question_four = input("Well done, getting high up is the smart thing to do. The coast looks clear but you can not be too 100% certain. Do you take a nap until to wait til it gets dark or do you climb down to continue your journey? Type nap or down").lower().strip()

    #        else answer == "approach" :
    #        print("uh-oh! Not the wisest decision, the tiger is not pleased. Game Over !!")
        

    #    else answer == "sleigh" : 
   #     print("Ummm, there are no hounds to pull the sleigh. Game over !!")

#else:
    #print("That is an incorrect response. Game Over.")
    