count = 0
dictionary_words = dict()                   # Initializes the dictionary
fhand = open('9.txt')
user_word = input("Enter the word")
if user_word in dictionary_words:
    print('True')
else:
    print('False')