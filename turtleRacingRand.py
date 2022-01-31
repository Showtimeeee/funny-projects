import turtle
import random
import time

screen = turtle.Screen()
screen.bgcolor('lightblue')

# We want two players in this game and the idea is
# that werever
player_one = turtle.Turtle()



# Color of player1
player_one.color('blue')

# Make this player a turtle!
player_one.shape('turtle')

# Player2 
player_two = player_one.clone()
# Colour of player two
player_two.color('red')

# Position p.
player_one.penup()
player_one.goto(-300, 200)
player_two.penup()
player_two.goto(-300, -200)

# Draw a finish line
player_one.goto(300, -250)
player_one.left(90)
player_one.pendown()
player_one.color('black')
player_one.forward(500)#("Arial", 8, "normal")
player_one.write('Finish', font=54)# Текст(надпись)

# Player1 go to start position
player_one.penup()
player_one.color('blue')
player_one.goto(-300, 230)
player_one.right(90) # Повернулась черепашка лицом к финишу)

# We need to make sure both p. have their pens down
player_one.pendown()
player_two.pendown()

# Crete values for the DIE
die = [1, 2, 3, 4, 5, 6]

# Let's create the game!
for i in range(30):
    if player_one.pos() >=(300, 250):
        player_one.goto(0, 0)
        player_one.write('I WIN!', font=24)
        print('Player One Win!')
        break
    elif player_two.pos() >=(300,-250):
        player_two.write('I WIN!', font=24)
        print('Player Two Win!')
        break
    else:
        die_roll = random.choice(die)
        player_one.forward(30*die_roll)
        time.sleep(1)
        die_roll2 = random.choice(die)
        player_two.forward(30*die_roll2)
        time.sleep(1)
# This keps the turtledrawing on the screen!
turtle.done()


