import time
import random
import os
from tkinter import Tk, filedialog

# Global variables
word_list = []
current_word_list = []
wordNumbers = 0
randomizeWords = False
timeTest = False
blindMode = False
wpmTest = False

def select_file():
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    file_path = filedialog.askopenfilename(
        title="Select a text file with words",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if file_path:
        with open(file_path, 'r') as file:
            words = [line.strip() for line in file if line.strip()]
        return words
    return None

def get_words_from_file():
    print("\nPlease select a text file using the file dialog...")
    words = select_file()
    while not words:
        print("No file selected or file was empty. Please try again.")
        words = select_file()
    return words

def get_words_manually():
    wordNumbers = int(input("Enter the number of words to be displayed: "))
    print(wordNumbers)
    words = []
    for w in range(1, wordNumbers + 1):
        word = input(f"Enter word {w}: ")
        words.append(word)
    return words

def calculate_wpm(chars_typed, time_taken):
    """Calculate Words Per Minute (5 chars = 1 word)"""
    if time_taken == 0:
        return 0
    words = chars_typed / 5
    minutes = time_taken / 60
    return round(words / minutes)

def run_test():
    global word_list, current_word_list, wordNumbers, randomizeWords, timeTest, blindMode, wpmTest
    
    print("\nWord input options:")
    print("1. Select a text file from your computer")
    print("2. Enter words manually")
    choice = input("Choose input method (1-2): ").strip()
    
    if choice == "1":
        word_list = get_words_from_file()
    elif choice == "2":
        word_list = get_words_manually()
    else:
        print("Invalid choice, defaulting to manual entry.")
        word_list = get_words_manually()
    
    wordNumbers = len(word_list)
    randomizeWords = input("Randomize word order? (y/n): ").lower() == 'y'
    timeTest = input("Record time taken? (y/n): ").lower() == 'y'
    wpmTest = input("Calculate WPM? (y/n): ").lower() == 'y'
    blindMode = input("Turn on blind mode? (y/n): ").lower() == 'y'

    start_time = time.time()
    chars_typed = 0
    current_word_list = random.sample(word_list, len(word_list)) if randomizeWords else word_list.copy()

    correct = 0
    for i, word in enumerate(current_word_list, 1):
        print(f"\nWord {i}/{wordNumbers}: {word}\n")
        user_input = input("Type the word: ")
        chars_typed += len(user_input)
        
        if user_input == word:
            correct += 1
            if not blindMode:
                print("Correct!")
        else:
            if not blindMode:
                print("Incorrect!")

    end_time = time.time()
    elapsed_time = end_time - start_time

    print("\nTest over.")
    print(f"Final score: {correct}/{wordNumbers} ({correct/wordNumbers:.0%})")
    
    if timeTest:
        print(f"Total time: {elapsed_time:.2f} seconds")
    
    if wpmTest:
        wpm = calculate_wpm(chars_typed, elapsed_time)
        print(f"Typing speed: {wpm} WPM")

def main():
    while True:
        print("\n--- Main Menu ---")
        print("1. Start New Test")
        print("2. Exit")
        choice = input("Choose (1-2): ").strip()
        
        if choice == "1":
            run_test()
            input("\nPress Enter to return to main menu...")
        elif choice == "2":
            print("Goodbye!")
            time.sleep(1)
            break
        else:
            print("Invalid choice, please enter 1 or 2")

if __name__ == "__main__":
    main()
