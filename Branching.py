"""
title: Branching
author: Nisha Seyed
date: 7/18/18 11:53 AM
"""

def food_order(choice,menu):
    if choice in menu:
        return "your order " + choice + " is on the menu and will be coming out soon"
    else:
        return "pick something else off the menu"

def guess_number(low,high):
    """tell user if guess is out of range"""
    guess = input(f"guess a number between {low} and {high}: ")
    guess = int(guess)
    if guess<= low:
        return f"no, {guess} is less than {low}"
    elif guess>= high:
        return f"no, {guess} is greater than {high}"
    else:
        return f"good! {low}< {guess}< {high}"

if __name__ == '__main__':
    #menu = ['pizza', 'salad', 'sushi', 'fajitas', 'omelets']
    #choice = input("Enter your choice of entree: ")
    #print(food_order(choice, menu))
    print(guess_number(5,20))

