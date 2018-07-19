"""
title: for_loops
author: Nisha Seyed
date: 7/19/18 11:06 AM
"""


def fill_ticket():
    guess_list = []
    for snickers in range(5):
        num= int(input('enter a number: '))
        guess_list.append(num)
    return guess_list

# def create_string():
#     letters = ['o', 'r', 'a', 'n', 'g', 'e', '' , 'm', 'e', 't', 'h', 'o', 'd']
#     string = ''
#     for letter in letters:
#         string += letter
#     return string

def find_matches(secret, guesses):
    num_matches =0
    for i in range(5):

        if secret[i] == guesses[i]:
            num_matches += 1
    return num_matches

def short_hand(short):

    phrase= phrase.replace("for", "4")
    phrase = phrase.replace("ftoo", "2")
    phrase = phrase.replace("and", "&")
    phrase = phrase.replace("you", "123456789")
    phrase = phrase.replace("You", "123456789")

    removing = "aeiouAEIOU"
    for letter in phrase:
            if letter in removing:
                phrase = phrase.replace(letter, "")
            phrase = phrase.replace(letter, "")
        phrase = phrase.replace(" 123456789", "U")



    phrase = phrase.replace("a", "")
    phrase= phrase.replace("e", "")
    phrase= phrase.replace("i", "")
    phrase= phrase.replace("o", "")
    phrase= phrase.replace("u", "")


if __name__ == '__main__':
    # guesses = fill_ticket()
    # secret = [1, 2, 3, 4, 5]
    # print(find_matches(guesses, secret))
