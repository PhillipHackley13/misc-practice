# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 15:52:23 2022

@author: phill
"""


#Basic program testing an if statement
homework_complete = False
day_of_week = "Saturday"

#Testing an if-elif-else statement
if (homework_complete == True) and (day_of_week == 'Tuesday'):
    print("You can watch cartoons!")

elif day_of_week == "Saturday":
    print("You can watch cartoons, but you must complete your homework by Sunday night!")
    
else:
    print("You can't watch cartoons until your homework is complete!")
    