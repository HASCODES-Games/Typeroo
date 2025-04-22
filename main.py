import time, pygame as pg, random, math

# Global variables to store test settings between runs
word_list = []
current_word_list = []
wordNumbers = 0
randomizeWords = False
timeTest = False

def run_test(new_test=True):
    global word_list, current_word_list, wordNumbers, randomizeWords, timeTest
    
    if new_test:
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
        randomizeWords = input("Would you like to randomize the order of the words? (y/n): ").lower()
        if randomizeWords == "y":
            randomizeWords = True
        elif randomizeWords == "n":
            randomizeWords = False
        else:  
            print("Invalid input, defaulting to no randomization.")
            randomizeWords = False

        timeTest = input("Would you like to record the time taken for the test? (y/n): ").lower()
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
        start_time = time.time()

    if randomizeWords or not new_test:  # Randomize if requested or repeating test
        current_word_list = random.sample(word_list, len(word_list))
    else:
        current_word_list = word_list.copy()

    w = 0
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
    print(f"You got {correct} out of {wordNumbers} correct.")
    accuracy = (correct / wordNumbers) * 100
    print(f"Accuracy: {accuracy:.2f}%")

    if timeTest:
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Total time taken: {elapsed_time:.2f} seconds")

# Main game loop
while True:
    run_test()
    
    while True:
        print("\nWould you like to:")
        print("1. Play this test again")
        print("2. Start a new test")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == "1":
            print("Repeating test...")
            time.sleep(1)
            run_test(new_test=False)
        elif choice == "2":
            print("Starting new test...")
            time.sleep(1)
            break  # Breaks out of inner loop to start new test
        elif choice == "3":
            print("Exiting...")
            time.sleep(1)
            exit()
        else:
            print("Invalid input, please try again.")
            continue
