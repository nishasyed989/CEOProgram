"""
title: Data_structures
author: Nisha Seyed
date: 7/19/18 10:17 AM
"""

import random



def name_generator(first_list, last_list):
    "should combine first and second lists"
    first = first_listxx
    last = last_list
    return f"{random.choice(first)} {random.choice(last)}"



if __name__ == '__main__':
    first_list = ["Joe", "Moe", "Bo", "LoLo", "Zo"]
    last_list = ["Smith", "Rodriguez", "Hernandez", "Doe", "Phillips"]
    print(name_generator(first_list, last_list))
