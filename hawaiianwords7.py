## CS 101
## hawaiianwords7.py
## Program 3
## Jacob Chambers
## jc7wc@mail.umkc.edu
##
## PROBLEM: Enter in a word to be pronounced in Hawaiian
##
## ALGORITHMN:
## 1.) Set a variable to True for main while loop.
## 2.) Set vowels variable = "AEIOU".
## 3.) Set each letter in vowels to a variable to each of their letter
##     pronunciations
## 4.) Set consonants = "PKHLMN".
## 5.) Set each letter in consonants to a variable to each of their letter
##     pronunciations.
## 6.) Set w and w groupings to variables with their respective pronunciations. 
## 7.) Set vowel groups to variables with their respective pronunciations.
## 8.) Set apostrophe = "'".
## 9.) Create while variable == True
## 10.) Make newstring = "".upper()
## 11.) Have user input what Hawaiian word they want to have pronounced.
## 12.) If word has any letter other a,e,i,o,u,p,k,h,l,m,n,",",w," ", then have
##      user input word until they meet this condition.
## 13.) Add for char in word:
## 14.) Add if char in vowels and use slicing to get one char in vowels for
##      every vowel and add newstring variable to the vowel sound.
## 15.) Do step 14 with all consonants.
## 16.) Set vowel groups to their respected pronunciations. For example, 
##      if "AU" in word:
##              newstring = newstring.replace("ah-oo-",au)
## 17.) if "W" in word[0], pronounce that "W" as w.
## 18.) Set w groupings with their respected pronunciations.
## 19.) If word has a "'" in it, that is a hard stop and seperates two letters.
##      So "a'o" would be pronounced "ah-oh", instead of "ow".
## 20.) Ask if user wants to type in another word Y,Yes,N,No. 
## 21.) If input is not Y,Yes,N,No, go back to step 20.
## 22.) If Y,Yes, go back to top of while loop and play again
## 23.) If N,No, exit the program.
##
################################################################################
################################################################################


playing = True

hawaiian_char = "AEIOUPKHLMN 'W"

while playing == True: #main loop
    z = 0 #variable for iterating through characters
 
    valid = False
    while not valid: #start of valid characters loop
        newString = "".upper() #pronunciation variable
        word = input('Enter a hawaiian word to pronounce ==> ').upper()
        word = word.upper()
        valid = True #exits valid characters loop
        for character in word: #iterates through each char to check if valid
            if not character in hawaiian_char: 
                print(character,"is not a valid Hawaiian character. A valid"\
                      " Hawaiian character is a,e,i,o,u,p,k,h,l,m,n,"\
                      "a space, or '(apostrophe)")
                valid = False #continues through loop asking for another word
                print()
        
    while z < len(word): #start of iterating thorugh each character loop

        if z == (len(word)-1): #last character loop
            if word[z] == "A": #A's
                z += 1 #adds 1 to variable and to move on to the next letter
                newString += "ah-" #adds pronunciation sound
                break #exits main loop and moves to print the pronunciation

            if word[z] == "E": #E's
                z += 1
                newString += "eh-"
                break

            if word[z] == "I": #I's
                z += 1
                newString += "ee-"
                break

            if word[z] == "O": #O's
                z += 1
                newString += "oh-"
                break

            if word[z] == "U": #U's
                z += 1
                newString += "oo-"
                break
            if word[z] == "P": #P's
                newString += "p"
                z += 1
                break

            if word[z] == "K": #K's
                newString += "k"
                z += 1
                break
                
            if word[z] == "H": #H's
                newString += "h"
                z += 1
                break

            if word[z] == "L": #L's
                newString += "l"
                z += 1
                break

            if word[z] == "M": #M's
                newString += "m"
                z += 1
                break

            if word[z] == "N": #N's
                newString += "n"
                z += 1
                break

        if word[z] == "W": #W's
            if z == 0: #if W is the start of a word
                newString += "w"
                z += 1
                continue #continues through iterating characters loop
            if z >= 1: #if W is after the start of a word
                if word[z-1] == "I": #if W is after letter I
                    newString += "v"
                    z += 1
                    continue
                if word[z-1] == "E":
                    newString += "v"
                    z += 1
                    continue
                if word[z-1] == "A":
                    newString += "w"
                    z += 1
                    continue
                if word[z-1] == "U":
                    newString += "w"
                    z += 1
                    continue
                if word[z-1] == "O":
                    newString += "w"
                    z += 1
                    continue
                else:
                    z += 1
                    continue
            else:
                z += 1 
                continue
                           
                                                 
        if word[z] == " ": #Spaces
            newString = newString.strip("-") + " " #deletes - from end up string
            z += 1
            continue
               
        if word[z] == "'": #Apostrophes 
            newString = newString.strip("-") + "'"
            z += 1
            continue
                     

        if word[z] == "A": #A's
            if word[z+1] == "U": #if A is before letter U
                newString += "ow-"
                z += 2 #counts AU as 2 characters and moves on with literating
                continue
            if word[z+1] == "I":
                newString += "eye-"
                z += 2
                continue
            if word[z+1] == "E":
                newString += "eye-"
                z += 2
                continue
            if word[z+1] == "O":
                newString += "ow-"
                z += 2
                continue
            else: #anything other than before U,I,E,O
                z += 1
                newString += "ah-"
                continue
                
        if word[z] == "E": #E's
            if word[z+1] == "I":
                newString += "ay-"
                z += 2
                continue
            if word[z+1] == "U":
                newString += "eh-oo-"
                z += 2
                continue
            else:
                z += 1
                newString += "eh-"
                continue
                
        if word[z] == "I": #I's
            if word[z+1] == "U":
                newString += "ew-"
                z += 2
                continue
            else:
                z += 1
                newString += "ee-"
                continue

        if word[z] == "O": #O's
            if word[z+1] == "I":
                newString += "oy-"
                z += 2
                continue
            if word[z+1] == "U":
                newString += "ow-"
                z += 2
                continue
            else:
                z += 1
                newString += "oh-"
                continue

        if word[z] == "U": #U's
            if word[z+1] == "I":
                newString += "ooey-"
                z += 2
                continue
            else:
                z += 1
                newString += "oo-"
                continue

        if word[z] == "P": #P's
            newString += "p"
            z += 1
            continue

        if word[z] == "K": #K's
            newString += "k"
            z += 1
            continue
            
        if word[z] == "H": #H's
            newString += "h"
            z += 1
            continue

        if word[z] == "L": #L's
            newString += "l"
            z += 1
            continue

        if word[z] == "M": #M's
            newString += "m"
            z += 1
            continue

        if word[z] == "N": #N's
            newString += "n"
            z += 1
            continue

        

        



    print("{} is pronounced {}".format(word,newString.capitalize()\
          .strip("-"))) #prints original word and how the word is pronounced
                                       

    

    while playing == True: #start of play again loop
        play_again = input("Do you want to enter another word? (Y,Yes,N,No) ==> ")
        play_again.lower()

        #if not Y,Yes,N,No, must enter in valid response and asks again
        if play_again != "yes" and play_again != "y" and \
           play_again != "no" and play_again != "n":
            print("you must enter Y,Yes,N or No")

        #goes back to starting loop and starts the game over
        if play_again in ('yes','y'):
            print()
            break

        #breaks out of loop and exits the program
        if play_again in ('no','n'):
            playing = False
            break    
            
                
