# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 13:08:26 2022

@author: phill
"""

#Program designed to allow user input into a story template.Creating a customizable story for each individual.


#Variables that will be used to collect user input for the story template
adjective = input("Enter one adjective: ").lower()
name_of_an_outdoor_game = input("Enter a name of one outdoor game: ").lower()
adjective_2 = input("Enter one adjective: ").lower()
name_of_friend = input("Enter a name of one of your friends: ").capitalize()
verb_ending_in_ing = input("Enter a verb ending in ing: ").lower()
adjective_3 = input("Enter one adjective: ").lower()

#Generic story template
story = (f'It was a {adjective} summer day at the beach. \
My friends and I were in the water playing {name_of_an_outdoor_game}. As a {adjective_2} \
wave came closer, my friend {name_of_friend} yelled,\
"Look! There\'s a jellyfish {verb_ending_in_ing}" \
{name_of_friend} ran out of the water and onto the sand.\
{name_of_friend} was afraid of {verb_ending_in_ing} jellyfish.\
The rest of us stayed in the water playing {name_of_an_outdoor_game} \
because {verb_ending_in_ing} jellyfish are {adjective_3}.')

print(story)