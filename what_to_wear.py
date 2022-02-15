# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 18:13:26 2022

@author: phill
"""

#Practice program with if-else-elif statements

#User input for current temperature
temperature = int(input("What is the current temperature?"))

#outfit chosen based on user input
if temperature >= 80:
    outfit = "shorts and pack your sunglasses"
    
elif temperature <= 79 and temperature >= 60:
    outfit = "light jacket"

else:
    outfit = 'a coat in addition to a hat, gloves, and scarf'


advice = (f'Today you should wear {outfit}')

print(advice)
    
    