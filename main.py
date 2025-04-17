import time, pygame as pg, random, math

#setup word list
wordNumbers = input("Enter the number of words to be displayed: ")
print(wordNumbers)
wordNumbers = int(wordNumbers)
w = 1
word_list = []
while w < wordNumbers + 1:
    word = input("Enter word " + str(w) + ": ")
    word_list.append(word)
    w = w + 1

#setup game settings
randomizeWords = input("Would you like to randomize the order of the words? (y/n): ")
if randomizeWords == "y":
    randomizeWords = True
elif randomizeWords == "n":
    randomizeWords = False
else:  
    print("Invalid input, defaulting to no randomization.")
    randomizeWords = False

timeTest = input("Would you like to record the time taken for the test? (y/n): ")
if timeTest == "y":
    timeTest = True
elif timeTest == "n":
    timeTest = False
else:
    print("Invalid input, defaulting to no time recording.")
    timeTest = False

# Initialize stopwatch variables
start_time = 0
end_time = 0

if timeTest:
    print("\nTest starting now...")
    start_time = time.time()  # Start the timer when the test begins

if randomizeWords:
    word_list = random.sample(word_list, len(word_list))

w = 0  # Changed to start from 0 to fix index issue
while w < wordNumbers:
    print("\n" + word_list[w] + "\n")
    wordWrite = input("")
    print(wordWrite)
    if wordWrite == word_list[w]:
        print("\nCorrect!")
    else:
        print("\nIncorrect!")
    w = w + 1

print("\nTest over.")

if timeTest:
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"\nTotal time taken: {elapsed_time:.2f} seconds")
