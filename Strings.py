"""
title: Strings
author: Nisha Seyed
date: 7/18/18 2:56 PM
"""
greeting = "how's your day"



def how_eligible(essay):
    "return how many categories are in a string"
    it = 0
    if "?" in essay:
        it += 1
    else:
        it += 0
    if '"' in essay:
        it =+ 1
    else:
        it +=0
    if "," in essay:
        it += 1
    else:
        it += 0
    if "!" in essay:
        it  += 1
    else:
        it += 0
    return it





if __name__ == '__main__':
    print(how_eligible('This? "Yes." No, not really!'))
    print(how_eligible('Really, not a compound sentence.'))
