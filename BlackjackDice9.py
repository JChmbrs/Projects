## CS 101
## blackjackdice9.py
## Program 2
## Jacob Chambers
## jc7wc@mail.umkc.edu
##   
## PROBLEM: Play a game of Blackjack using Dice with a computer and yourself          
##
## ALGORITHMN:
##    1.) Start off by welcoming the player to the game
##    2.) Have the player enter in the money value they want in chips.
##        2a.) Cannot be <=0, any other number will work and prompt user
##             to enter in value again.
##        2b.) Convert chip_total_str to an integer.     
##    3.) Have the player enter in how much they want to wager each round.
##        3a.) Value must be >=0 and <= the amount they have left and prompt
##             user to enter in value again.
##        3b.) Convert bid_amount_str to an integer.
##    4.) Have the dealer roll two dice and add them together.
##    5.) Have user roll two dice and add them together.
##    6.) Ask if user want to roll again
##        6a.) Must enter Y,Yes,N,No, if enters anything else, prompt user what
##             they must enter and ask them to roll again.
##    7.) Give option to stop rolling and stay (when user types N or NO)
##        7a.) If player stays, have the dealer roll until he ties you or he
##             goes over 21.
##            7aa.) If dealer ties, prompt the user this and tell them its a
##                  push, also prompt them how much they have left and go back
##                  to step 3.
##            7ab.) If dealer goes over 21, prompt the user how much they won
##                  (which will be their wager amount) and tell them how much
##                  they have in their pot and go back to step 3.
##    8.) If user goes over 21, then they lose their wager amount. Prompt
##        that they busted (went over 21), how much they lost that round, how
##        much they have left in the pot, and go back to step 3.
##    9.) Game ends when user has 0$ left in their pot.
##        9a.) When game ends, tell user how many rounds they played and
##             their highest pot total during the game. 
##    10.) Ask user if they want to play again.
##        10a.) must be Y,Yes,N,NO just like in step 7 and cannot be anything
##             else.
##            10aa.) If Y or Yes, then loop back to step 2.
##            10ab.) If N or No, break out of the loop and end the program.
##
################################################################################
################################################################################

print("Welcome to Blackjack Dice!")
print()

import random

playing = True

while playing == True: #starting loop
    
    highest_total = 0 #highest chip total value 
    rounds = 0  #how many rounds you've played
    chip_total_str = input("Enter the amount of money you want in chips. ==> $")
    chip_total = int(chip_total_str) #converts str to int
    if chip_total <= 0: #chip_total must be greater than 0
        print("The amount must be greater than 0")
        continue

    while chip_total > 0: #main loop for game
       
        if highest_total < chip_total: #calculates highest chip total
            highest_total = chip_total

        bid_amount_str = input("Enter the amount you want to wager. ==> $")
        bid_amount = int(bid_amount_str)

        if bid_amount <= 0: 
            print("The wager must be greater than zero")
            continue                 
        
        if bid_amount > chip_total:
            print("The wager cannot be greater than the amount you have" \
                  " in the pot")
            continue

        #starts the game
        if bid_amount > 0 and bid_amount <= chip_total:

            rounds += 1 #adds +1 round each round

            #rolls random number between 1 and 6      
            dealer_roll_1 = random.randint(1,6)
            dealer_roll_2 = random.randint(1,6)
            your_roll_1 = random.randint(1,6) 
            your_roll_2 = random.randint(1,6)
    
            print()

            #shows what the dealer rolled 
            print("Dealer rolled a",dealer_roll_1,"and a",dealer_roll_2,"for a"\
                  " total of",(dealer_roll_1 + dealer_roll_2))

            print()

            #shows what you rolled 
            print("You rolled a",your_roll_1,"and a",your_roll_2,"for a total"\
                  " of",(your_roll_1 + your_roll_2))

            #sum of your roll and dealers roll
            dealer_sum = (dealer_roll_1 + dealer_roll_2)
            your_sum = (your_roll_1 + your_roll_2)

            #allows entrace to new while loop
            rolls_again = True

            #start of your rolls
            while rolls_again == True:
                
                roll_again = input("Do you want to roll again? (Y,YES,N,NO)"\
                                   " ==> ")
                roll_again.lower() #converts uppercase strings to lowercase

                #must enter in y,yes,n,no if not goes back and asks again
                if roll_again != "yes" and roll_again != "y" and \
                   roll_again != "no" and roll_again != "n":
                    print("you must enter Y,Yes,N or No")

                #if you want to roll again, rolls 1 dice and gives your sum
                #then goes back to asking you if you want to roll again
                if roll_again in ('yes','y'):
                    number = random.randint(1,6)
                    number = int(number)
                    your_sum += number
                    your_sum = int(your_sum)
                    print("you rolled a",number,"for a total of",your_sum)
                    
                #if you roll over 21, you lose wager amount 
                if your_sum > 21:                    
                    print("You Busted, I'm so sorry")
                    print()
                    print("The dealer won this round, you've lost your $"\
                        ,bid_amount,"wager")
                    print()
                    chip_total = (chip_total - bid_amount)
                    print("You now have $",chip_total,"in the pot")
                    rolls_again = True
                    break     

                #if you decide not to roll again, breaks out of loop and into
                #the next loop
                if roll_again in ('no','n'):
                    print("you stayed on",your_sum)
                    print()
                    rolls_again = False #brings you to not rolling again loop
                    break
    
            #loop that processes not rolling again inputs
            while rolls_again == False:
                #dealer keeps rolling dice until an if condition is met
                number = random.randint(1,6) #dice roll for dealer
                number = int(number) 
                dealer_sum += number #adds dice roll to dealers sum
                dealer_sum = int(dealer_sum)
                print("The Dealer rolled",number,"for a total of",\
                       dealer_sum)               

                #when dealer rolls over 21, you win your bid amount and goes
                #back to main loop
                if dealer_sum > 21:
                    print("Congratulations, you won $",bid_amount,)
                    print()
                    chip_total = (bid_amount + chip_total)                    
                    print("You now have $",chip_total,"in the pot")
                    break
                
                #if dealer rolls the same sum as you, its a tie and goes
                #back to main loop
                if dealer_sum == your_sum:
                    print("You tied the dealer, it's a push")
                    print()
                    print("You now have $",chip_total,"in the pot")                           
                    break

                #if dealer rolls a sum higher than yours, dealer wins, you lose
                #your wager amount and goes back to main loop
                if dealer_sum > your_sum:
                    print("The dealer won this round, you've lost your $"\
                          ,bid_amount,"wager")
                    print()
                    chip_total = (chip_total - bid_amount)
                    print("You now have $",chip_total,"in the pot")
                    break               

                #if dealer under 21 and none of the above conditions are met
                #continue with the loop (dealer keeps rolling)
                if dealer_sum < 21:
                    continue

    #when your_sum = 0
    print()
    print("You ran out of money")
    print("You played",rounds,"rounds. Your highest pot was",highest_total)
    print()

    #asking to play again loop
    while chip_total == 0:
        play_again = input("Do you want to play again? (Y,Yes,N,No) ==> ")
        play_again.lower()

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
            
            
                    
        
    



                   
                    

            
            
                        
                


                        
            

        
       
        
    
        
       
    

    

  
   


 

    
        

        
        
    
    
    
              
    
       
        
   
        
   
        
         
    
            
     
    
    
  
       

   

      
    


    
        
    


    
    
            



    

