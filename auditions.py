# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 10:50:40 2022

@author: phill
"""

#Goal of the program:School Musical Sign-Ups
#Students have the option to sign up for different positions 
#Collect data and store them in empty dictionaries to later present 


#Dictionaries that stores the audition sign-ups 
auditions = { 
    "Principal" : { 
        },
    "Teacher" : {
        },
    "Troublemaker" : {
        },
    "Students" : {
        }
    }

#Function for the sign-up process
def sign_up():
    name = input('What is your name?').capitalize()
    grade = input('What is your grade? (Please respond with a number) ')
    role = input('''What is your preferred role? Please 
             select a number from the following options:
                 [1]Principal
                 [2]Teacher
                 [3]Troublemaker
                 [4]Student
                 ''')

    
                 
    if role == '1' :
        auditions['Principal'][name] = grade

    elif role == '2':
        auditions['Teacher'][name] = grade
        
    elif role == '3':
        auditions['Troublemaker'][name] = grade 
    
    else:
        auditions['Students'][name] = grade
#For loop that calls the signup function to fill the empty dictionaries        
for i in range(5):
    sign_up()

#Printout for the list of students signed up to audition
print("Sign-ups for 'A Day without a Principal' are now closed'")

print("Role : Principal")
for student, grade in auditions['Principal'].items():
    print(student, grade)
print("Role : Teacher")
for student, grade in auditions['Teacher'].items():
    print(student, grade)
print("Role : Troublemaker")   
for student, grade in auditions['Troublemaker'].items():
    print(student, grade)
print("Role : Student")   
for student, grade in auditions['Students'].items():
    print(student, grade)
