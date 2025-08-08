# here i will get data from already prepared API called DATAMUSE API 

# the library we will use is requests is requests 
import requests

def get_Words() :
   response = requests.get("https://api.datamuse.com/words?sp=?????")   
  
   data = response.json()
  
#  to get the words has only five letters 
# initialize array of suitable words 
   words =[]
   for WORD in data:
        word = WORD['word']
        if len(word) == 5:  
            words.append(word)
    
   return words

the_filterd_data = get_Words()

# test the filtered data 
print(the_filterd_data)

