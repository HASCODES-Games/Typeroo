import time, pygame as pg, random, math

#setup word list
wordNumbers = input("Enter the number of words to be displayed: ")
print(wordNumbers)
wordNumbers = int(wordNumbers)
w=1
word_list = []
while w<wordNumbers+1:
    word = input("Enter word " + str(w) + ": ")
    word_list.append(word)
    w=w+1

#setup game settings
randomizeWords = input("Would you like to randomize the order of the words? (y/n): ")
if randomizeWords == "y":
    randomizeWords = True
elif randomizeWords == "n":
    randomizeWords = False
else:  
    print("Invalid input, defaulting to no time recording.")
    recordTime = False

if randomizeWords == False:
    w=1
    while w<wordNumbers:
        print("\n" + word_list[w] + "\n")
        wordWrite = input("")
        print(wordWrite)
        if wordWrite == word_list[w]:
            print("\nCorrect!")
        else:
            print("\nIncorrect!")
        w=w+1
    print("\nTest over.")
elif randomizeWords == True:
    word_list = random.sample(word_list, len(word_list))
    w=1
    while w<wordNumbers:
        print("\n" + word_list[w] + "\n")
        wordWrite = input("")
        print(wordWrite)
        if wordWrite == word_list[w]:
            print("\nCorrect!")
        else:
            print("\nIncorrect!")
        w=w+1
    print("\nTest over.")
