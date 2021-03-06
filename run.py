# To allow time delay in game
import time

# Upper and lower case that the player may use
answer_A = ["A", "a"]
answer_B = ["B", "b"]

# To reduce duplication of code
required = ("\nUse only A or B\n")

# Intro the player
print("""You have opened the doors of the unknown. If you choose to embark
upon this journey there will be faced with 2 choices at every turn.
There is only one correct answer. Your fate is in your hands only!""")

# Player promt to type name to play


def get_name():
    """ Player prompted to enter name to begin playing. """
    name = input("Enter your name to play: ").capitalize().strip()

    if name != '':
        print("Hello", name, "you have now entered the world of Adventure!!")

    else:
        print("""you must enter a name to play""")
        get_name()


# Function added to reduce duplication of code unecessairly.
# While loop added to prompt player when their repsonse entry is incorrect.

def get_response():
    """ Player promted to enter A or B """
    is_not_okay = True
    while is_not_okay:
        print("Please enter A or B")
        choice = input(">>> ").strip().upper()
        if choice in answer_A or choice in answer_B:
            is_not_okay = False
    return choice


def game():
    """ Main section of the game. The player is asked a question at a time with
    2 options to choose from
    """

    # Question 1
    print("""You close your eyes in anticipation of the game starting.
    Well it has started and you feel a cold breeze enveloping you.
    You open your eyes to find snow miles on end,
    and something moving in the distance.
    A polar bear appears charging at you some 50 meters away.""")

    time.sleep(2)

    print("""You have 2 options, start running or lay on the ground
and play dead.
    Type:
    A. Run
    B. Play dead """)
    choice = get_response()

    # Below are the consequences of the answers to question 1
    if choice in answer_A:
        print("Did you really think you could out run a polar bear?\
The bear got you!! Game over")
        game_over(True)

    else:
        option_play_dead()

    # Question 2


def option_play_dead():
    print("""That was a clever move. The coast is now clear,
you start walking and 5 minutes later you come accross a
paddle boat and a sleigh. """)

    time.sleep(3)

    print("""Pick one to continue your journey.
Type:
    A. Paddle
    B. Sleigh """)
    choice = get_response()

    # Below are the consequences of the answers to question 2
    if choice in answer_A:
        option_paddle()

    else:
        print("""Ummm, there are no hounds to pull the sleigh. While you were
messing around you got eaten by a wondering bear.  Game over !!""")
        game_over(True)


def option_paddle():
    # Question 3
    print(""""That turned out to be a wise choice because you soon
come across a river and use your boat to get across. Now on
the other side you find a jungle, deep in this jungle you bump
into a tiger. Do you climb a tree or approach the tiger to
reassure him that you are friendly?""")

    time.sleep(2)

    print("""Type:
  A. To climb
  B. To approach """)
    choice = get_response()

    # Below are the consequences to the answers to question 3
    if choice in answer_A:
        option_climb()

    else:
        print("uh-oh! Not the wisest decision, the tiger is not pleased\
and eats you alive. Game Over !!")
        game_over(True)


def option_climb():
    # Question 4
    print(""""Well done, getting high up is the smart
thing to do. The coast looks clear but you can not be too 100% certain.
Do you take a nap until it gets dark or do you climb
down to continue your journey?""")

    time.sleep(2)

    print("""Type:
  A. To nap
  B. To climb down """)
    choice = get_response()

    # Below are the consequences to the answers to question 4
    if choice in answer_A:
        print("""Oh dear, you fell off whilst sleeping and fall to
        your death! Game over!!""")
        game_over(True)

    else:
        option_climb_down()


def option_climb_down():
    # Question 5
    print("""You make your way through. It has been a long journey and you
    would like nothing but to find a lucky break out out of this chaos.
    You see something shining in the distance and pick up your pace to
    to get to it quicker. Your eyes light up as you realsie it is
    a treasure chest with a key. You imagine what could be inside this
    chest. As your minds starts racing you realise it is time
    to make a choice...""")

    time.sleep(2)

    print("""Do you open it or keep walking?
Type
    A. To open it
    B. To keep walking """)
    choice = get_response()

    # Below are the consequences to the answers to question 5
    if choice in answer_A:
        print("Uh-oh, you have unleashed a king cobra aarggghhhh!!\
Game over!!")
        game_over(True)

    else:

        option_keep_walking()


def option_keep_walking():
    print("""You followed your instincts and kept the lid on
the treasure box. Who would leave a
chest full of treasure in thh jungle anyway?/n
You see a door, no walls around it. This time, there are no options.
You will be walking through it""")
    game_over(False)


def game_over(is_lost):
    if is_lost:
        print("""Thanks for playing the aventure, though you can't hear me as
you're dead - You lose! """)

    else:
        print("""You made it!! Well done for reaching the end! If I go on an adventure I
sure hope it's with you! You win!""")

    exit()


get_name()


game()
