import random
words = ["apple", "banana", "cherry", "dog", "elephant", "flower", "grape", "house", "island", "jungle",
             "keyboard", "lemon", "mountain", "notebook", "orange", "pencil", "queen", "rainbow", "sunshine", "tiger"]
shuffled = words.copy()
counter = 0

while True:
    if(shuffled):
        random_word = random.choice(shuffled)
        word_input = input("enter random word: ")
        if(random_word == word_input):
            print("correct")
            counter = counter + 1
        else:
            print("wrong")
        
        shuffled.remove(random_word)
    else:
        print(str(counter) + " out of " + str(len(words)))
        break