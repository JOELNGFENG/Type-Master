import random
words = ["bowl","aaa","three"]
shuffled = words.copy()
counter = 0

while True:
    if(shuffled):
        random_word = random.choice(shuffled)
        input = input("enter random word: ")
        if(random_word == input):
            print("correct")
            counter = counter + 1
        else:
            print("wrong")
    else:
        break