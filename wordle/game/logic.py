#  get the data filterd from Api 
from utils.THE_FETCHING import get_Words
import random

# now to seletct thr word of test 
def select_word():
    words = get_Words()
    TEST_WORD = random.choice(words)
    return TEST_WORD

# //////
mY_Target = select_word()
print(mY_Target)
    
# /////////////////////////////
# compare the target word with the user input(guess)

def compare_word(user_input, target_word):  
  for i in range(5):
        if (guess[i] == Target[i]):
        #   right letter in right position 
              return "Green"
        elif (guess[i] in mY_Target):
            #   right letter in wrong position
            return  "orange "
        else :
        #   wrong letter
            return "red"
            
            
def play_game ():
    Target = select_word()
    filterd_data = get_Words()
    no_of_Attempts = 6 
    # to keeep track  , i will make it like a list od tuples 
    # each tuple will have two values the guess and the feedback 
    history = []
    while no_of_Attempts > 0:
            guess = input("Guess the word : ").lower()
            if len(guess) != 5 :
                print("Please enter word of 5 leters ")
                continue
            elif guess not in filterd_data :
                print(" invalid word  ")
                continue
            TEST = compare_word(guess, Target)
            history.append((guess ,TEST))
            
 # print the result ti the user , (the test and guess word )
# dispaly all his guesses 

        # /////
    print("\nYour guesses:")
    for g, f in history:
        print(f"{g} → {f}")

        if guess == target_word:
          print(" BRAVO ... You guessed it")
          break

        no_of_Attempts = no_of_Attempts -1 
        if no_of_Attempts == 0  and  guess != Target :
          print("Game Over , you are loser  ,  The word was " + Target )
            
    
                
                

        
       
    
    