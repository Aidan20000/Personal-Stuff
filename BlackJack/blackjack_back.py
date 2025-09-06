from utils import *
from tkinter import *

root = Tk()

def play():
    # Starting Cards
    card1 = Card()
    card2 = Card()

    # Tracks total score and card values
    totval = card1.val + card2.val
    vals = [card1.val, card2.val]
    
    # Starts Gameplay Loop
    print(f"Your total is {totval}, would you like to keep pulling (y/n)")
    decision = input("")

    # Generates cards when the player wants
    totval = gameplay_loop(totval, decision, vals, root)

    # Dealers total
    opp = random.randint(15, 21)

    # Disables ending text if player went over the 21
    if totval <= 21:
        tell_win_loss(opp, totval)

play()