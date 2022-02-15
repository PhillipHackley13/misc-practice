# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 11:58:24 2022

@author: phill
"""
#Program to incorportate lists, the random module, and nested loops

#User has a set of starting marbles with the goal of adding green marbles to their collection
#User can select 5 marbles per try and have 5 tries per day.

import random

#starting collection of marbles
collection = ['red','pink', ' orange', 'red', 'pink', 'yellow', 'pink','yellow']

#picking random marbles out of the secret bag to add to the collection
secret_bag = ['pink', 'blue', 'green', ' orange', ' red', 'purple', ' green', 'blue', \
              'blue', 'red', 'green', 'purple', 'yellow', 'red', 'pink', 'red', 'green', 'yellow']

marbles_chosen = []

#5 marbles is the maximum amount allowed to be taken from the secret bag variable
tries_remaining = 5

#Marbles randomly chosen from the secret bag and stored in the selection variable. 
#If the marble is green it will be added to the collection list and removed from the secret bag

for x in range(6):
    if tries_remaining > 0:
        selection = random.choice(secret_bag)
        marbles_chosen.append(selection)
        tries_remaining -= 1
        if selection == 'green':
            collection.append(selection)
            secret_bag.remove(selection)
            if('green' in collection):
                print(f'Awesome! You found a green marble. If you would like another marble, you have \
                      {tries_remaining} pick(s) left' )
                break
                
    else:
        print('Sorry, you are out of tries. Please come back tomorrow and try again!')
        
print(f'Here are all the marbles that were chosen: {marbles_chosen}')

print(f'My current collection has {collection} colored marbles')