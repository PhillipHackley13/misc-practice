# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 10:03:01 2022

@author: phill
"""

#The goal of the program is to randomly 7 players from the available pool player to assemble a kickball team



import random 
#Available player pool is established
available_players = ['Anastasia', 'Eli', 'Jamal', 'Jada', 'Theo', 'Michelle', 'Adam', 'Rhea', 
           'Charlie', 'Jasmine', 'Marley', 'Kenji', ' Sydney', 'Yara']
#team 1 is established
jaleesas_team = ['Jaleesa']
#team 2 is established
rahims_team = ['Rahim']

#While loop continues to randomly choose and then add chosen players to Jaleesas's team. Chosen players are then removed from the available player pool

while len(jaleesas_team) < 8:
    player_selected = random.choice(available_players)         
    jaleesas_team.append(player_selected)
    available_players.remove(player_selected)

#Left over players from the available player pool are then added to Rahim's team
rahims_team.extend(available_players)

#Final teams are printed and formatted to remove brackets and present more naturally
print("Jaleesas Team:")
print(*jaleesas_team, sep = " , ")
print("Rahims Team:")
print(*rahims_team, sep = " , ")