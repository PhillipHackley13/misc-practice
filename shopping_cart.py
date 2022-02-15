# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 09:33:28 2022

@author: phill
"""

#Program designed to calculate the total cost of individual gardening supplies with sales tax included



#Setting variables that allow the user to input the quantinty of each item purchased
flower_pot = int(input("How many flower pots would you like?:"))
flower_seeds = int(input("How many flower_seeds would you like?:"))
bag_of_soil = int(input("How many bags of soil would you like?:"))


#Setting variable price of each individual item
flowerpot_price = 4.00
flowerseeds_price = 1.00
bagofsoil_price = 5.00

#Setting the tax rate that will be applied to each individual item
tax_rate = .06

#Multiplying the quantity defined by the user with the set price of each individual item
cost_of_items = (flower_pot * flowerpot_price + flower_seeds * flowerseeds_price + bag_of_soil * bagofsoil_price) 
#Multiplying the cost_of_items by the tax rate and then adding the cost_of_items to find our final price with tax applied
total_cost = (cost_of_items * tax_rate) + cost_of_items
#Displaying the total cost to the user
print(f"The total cost of items:{total_cost}")

