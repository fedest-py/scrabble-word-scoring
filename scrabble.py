#******************************************************************************
# scrabble.py
#******************************************************************************
# Name: Eduardo Estevs
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#
#

################################################################################
#
# POINTS
#
################################################################################
points = {'a':1,
          'b':3,
          'c':3,
          'd':2,
          'e':1,
          'f':4,
          'g':2,
          'h':4,
          'i':1,
          'j':8,
          'k':5,
          'l':1,
          'm':3,
          'n':1,
          'o':1,
          'p':3,
          'q':10,
          'r':1,
          's':1,
          't':1,
          'u':1,
          'v':4,
          'w':4,
          'x':8,
          'y':4,
          'z':10}

#open the file
all_words = open('words_eng.txt', 'r')


#two empty lists for the scores adn respective words
score_list = []

word_list = []

#loop goes trough the file line by line
for word in all_words:
    #'empty' variables to build the score and the respective word
    the_word = ''
    score = 0
    for letter in word:
        #all character but the '\n'
        if letter != '\n':
            score += points[letter]
            the_word += letter
    #append the score and the letter to their list        
    score_list.append(score)
    word_list.append(the_word)
    
all_words.close()

#index variable will increase when the loop runs
index_count = 0
#stores the index of the highes score
max_index = 0

#loop compares the known max score with all values on the score list and saves the idx of the highest
for score in range(len(score_list)-1):
    index_count += 1
    if score_list[max_index] < score_list[index_count]:
        max_index = index_count
        
#return the word with the highest score
print(f'Most valuable word: {word_list[max_index]}')



