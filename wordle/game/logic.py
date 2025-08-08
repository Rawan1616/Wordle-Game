#  get the data filterd from Api 
from wordle.game.utils.THE_FETCHING import get_Words
import random

# now to seletct thr word of test 
def select_word():
    words = get_Words()
    TEST_WORD = random.choice(words)
    return TEST_WORD

# //////
Target = select_word()
print("//////the target is ://////" + Target)
    
# /////////////////////////////
# compare the target word with the user input(guess)

def compare_word(user_input, target_word): 
    total = []
    for i in range(5):
        if (user_input[i] == target_word[i]):
            # return "Green"
            total.append("Green")
        #   right letter in right position 
        elif (user_input[i] in target_word):
            #   right letter in wrong position
            # return  "orange "
            total.append("orange")
        else :
        #   wrong letter
            # return "red"
            total.append("red")
            
    return total 
            
            
def play_game ():
    filterd_data = get_Words()
    no_of_Attempts = 6 
    # to keeep track  , i will make it like a list od tuples 
    # each tuple will have two values the guess and the result of thid guess
    history = []
    while no_of_Attempts > 0:
                # i have added strip in debugging to remove any whitespaces 
            guess = input("Guess the word : ").strip().lower()
            if len(guess) != 5 :
                print("Please enter word of 5 leters ")
                continue
            elif guess not in filterd_data :
                print(" invalid word ")
                continue
            TEST = compare_word(guess, Target)
            history.append((guess ,TEST))
            no_of_Attempts = no_of_Attempts -1
            print("Your guesses:")
            for g, f in history:
        # /////////
                print(f"{g} → {f}")
                
                if guess == Target:
                  print(" BRAVO ...,,,,,,,,,, You guessed it")
                  break
                 

                if no_of_Attempts == 0  and  guess != Target :
                  print("Game Over ...., you are loser  ,....  The word was " + Target )
             
            
 # print the result ti the user , (the test and guess word )
# dispaly all his guesses 

        # /////
       
            
    
                
                

        
       
    
    