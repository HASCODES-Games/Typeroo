import time, pygame as pg, random, math

def run_test():
    # Setup word list
    wordNumbers = input("Enter the number of words to be displayed: ")
    print(wordNumbers)
    wordNumbers = int(wordNumbers)
    w = 1
    word_list = []
    while w < wordNumbers + 1:
        word = input("Enter word " + str(w) + ": ")
        word_list.append(word)
        w = w + 1

    # Setup game settings
    randomizeWords = input("Would you like to randomize the order of the words? (y/n): ")
    if randomizeWords.lower() == "y":
        randomizeWords = True
    elif randomizeWords.lower() == "n":
        randomizeWords = False
    else:  
        print("Invalid input, defaulting to no randomization.")
        randomizeWords = False

    timeTest = input("Would you like to record the time taken for the test? (y/n): ")
    if timeTest.lower() == "y":
        timeTest = True
    elif timeTest.lower() == "n":
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
        current_word_list = random.sample(word_list, len(word_list))
    else:
        current_word_list = word_list.copy()

    w = 0  # Start from 0 to fix index issue
    correct = 0
    while w < wordNumbers:
        print("\n" + current_word_list[w] + "\n")
        wordWrite = input()
        print(wordWrite)
        if wordWrite == current_word_list[w]:
            print("\nCorrect!")
            correct += 1
        else:
            print("\nIncorrect!")
        w = w + 1

    print("\nTest over.")

    if timeTest:
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"\nTotal time taken: {elapsed_time:.2f} seconds")
    print("You got " + str(correct) + " out of " + str(wordNumbers) + " correct.")
    accuracy = (correct / wordNumbers) * 100

# Main game loop
while True:
    run_test()
    
    print("\nWould you like to play again? (y/n): ")
    playAgain = input().lower()
    if playAgain == "n":
        print("Exiting...")
        time.sleep(1)
        break
    elif playAgain != "y":
        print("Invalid input, exiting...")
        time.sleep(1)
        break
    else:
        print("Restarting...")
        time.sleep(1)
