#Authored by Tyler Rincón Frankum [ki5bzg@shsu.edu]
#Created 18 JAN 2023
#Last updated 18 JAN 2023

#This program prompts the user for a character then returns the Unicode value for that character. 

#import the Unicode character databse

import unicodedata
import string

#storing values for later use up here because I'm a heathen

characterenteredstate = 0

#Prompt the user for the character they wish to lookup

while (characterenteredstate) < 1:
    lookupcharacter = input("Please enter the character you wish to lookup: \n")
    #This is to make sure the user only inputs one character.
    if len(lookupcharacter) > 1:
        print('\nPlease only enter one character \n')
    else:
        characterenteredstate = 1

#Lookup and store the results from unicodedata and the built in ord function into strings for later use. 

else:
    charactername = unicodedata.name (lookupcharacter)
    charactercoderaw = ord(lookupcharacter)
    characercodehex = format(charactercoderaw, '#06x')

#Put it all together using the variables we collected and then print it out. 

    constructedoutputstring = f"\n{lookupcharacter} is known as {charactername} and has a unicode hexidecimal value of {characercodehex}"
    
    print (constructedoutputstring)
