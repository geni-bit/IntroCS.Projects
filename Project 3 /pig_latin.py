# IntroCS Project 3: Task 1  - Pig Latin Converter

# asking the user for a word in Pig Latin
piglatin = input("Enter a word in Pig Latin: ")

# spilt the word into two strings by the position of hyphen
word_list = piglatin.split("-")

# making the varaibles for the each of the strings
first_string = word_list[0]
second_string = word_list[1]

# removing the ay at the end of the second string
remover = second_string[:-2]

# Putting the the two strings to togther 
english_word = remover + first_string

# printing the english word 
print(english_word)
