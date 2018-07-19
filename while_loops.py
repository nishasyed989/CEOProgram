"""
title: while_loops
author: Nisha Seyed
date: 7/19/18 2:16 PM
"""
import math
import random

def guess_number(low, high):

    guess= input(f"give number between {low} and {high}: ")
    guess= int(guess)
    comp_guess = random.randint(low, high)

    while guess != comp_guess:
        num_guess=0
        num_guess += 1
        if guess < low:
            return f"no, {guess} is less than {low}."
        else:
            return f" no, {guess} is higher than {high}."

    if guess == comp_guess:

        print("correct")

guess_number(1, 5)
