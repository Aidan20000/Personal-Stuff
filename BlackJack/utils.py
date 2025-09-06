import random
from tkinter import *
from PIL import ImageTk, Image

def find_max(arr):
    max = arr[0]
    for num in arr:
        if num > max:
            max = num
    return max

class Card:
    def __init__(self):
        self.val = random.randint(1, 10)
    
    def tellVal(self):
        print(f"Youre card was a {self.val}!")

def gameplay_loop(totval, decision, vals, root):
    while decision == "y" and totval <= 21:
        newcard = Card()
        pic = "OIP" + str(newcard.val) + ".jpg"
        img = ImageTk.PhotoImage(Image.open(pic))
        label = Label(image=img)
        label.pack()
        if newcard.val == 1:
            print("You Got an ace!")
            print("Would you like it to be an 1 or an 11")
            val = input("")
            newcard.val = int(val)
        totval = totval + newcard.val
        if totval > 21:
            print(f"You Lost, you pulled a {newcard.val} so your score was {totval}!")
            return totval
        vals.append(newcard.val)
        newcard.tellVal()
        print(f"Your total is {totval}, would you like to keep pulling (y/n)")
        decision = input("")
    return totval

def tell_win_loss(opp, totval):
    if opp > totval:
        print("You Lost!")
        print(f"Dealers Score: {opp}")
        print(f"Your score: {totval}")

    elif opp == totval:
        print("You Tied!")
        print(f"Your score: {totval}")
        print(f"Dealers Score: {opp}")

    else:
        print("You Won!")
        print(f"Your score: {totval}")
        print(f"Dealers Score: {opp}")