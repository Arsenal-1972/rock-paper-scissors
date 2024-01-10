#
# ROCK, PAPER, SCISSORS - Iterācija 2
# 
# 4. Pārkopēt šeit iepriekšējo failu, modificēt spēli no iepriekšēja faila, lai ir pieci raundi un beigas rādas cik sanāca vinnēt (izmantot for loop, https://www.w3schools.com/python/python_for_loops.asp)
# 5. [Bonus Level] Izmantot ne vairāk par trīs if/else rezultāta skaitīšanai (var izmantot ciparu starpību)
# 6. [UNSTOPPABLE] Pievieno papildus ieročus Rock-Paper-Scissors-Spock-Lizard (https://en.wikipedia.org/wiki/Rock_paper_scissors#Additional_weapons)
# 
ROCK = "1"
SCISSOR = "2"
PAPER = "3"


print("Welcome to Rock, Paper, Scissors!")
print("Please select number from 1 to 3")
option = input("Select number")
print("You have selected" + option)
import random

randint = str(random.randint(1, 3))
print("Computer selected" + randint)

if option == ROCK: 
    if randint == SCISSOR: 
        print("You won")
    elif randint == PAPER:
        print("You lost")
    elif randint == ROCK:
        print("Draw")
if option == PAPER: 
    if randint == ROCK: 
        print("You won")
    elif randint == SCISSOR:
        print("You lost")
    elif randint == PAPER:
        print("Draw")
if option == SCISSOR: 
    if randint == PAPER: 
        print("You won")
    elif randint == ROCK:
        print("You lost")
    elif randint == SCISSOR:
        print("Draw")     