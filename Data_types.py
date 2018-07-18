"""
title: Data_types
author: Nisha Seyed
date:  
"""""

print(type("NISHA"))
print(type(int("150")))


def add_tip(total, tip_percent):
    # return the total amount including tip
    tip = tip_percent * total
    return total + tip

x =add_tip(30, .2)
x += 5

def age_calculator(current_year, birth_year):
    '''returns users birth age'''
    age= current_year- birth_year
    return age

def mean(a, b, c):

    '''finding average of three numbers'''
    return (a+b+c)/3




if __name__=='__main__':

    print(age_calculator(2018,2003))
    print(mean(4,7,8))