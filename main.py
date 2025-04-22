import time
import random
import os
from tkinter import Tk, filedialog
from tkinter.messagebox import showinfo

def select_file():
    root = Tk()
    root.withdraw()  # Hide the main window
    root.attributes('-topmost', True)  # Bring dialog to front
    
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

def run_test(new_test=True):
    global word_list, current_word_list, wordNumbers, randomizeWords, timeTest
    
    if new_test:
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

    start_time = time.time() if timeTest else 0
    current_word_list = random.sample(word_list, len(word_list)) if randomizeWords else word_list.copy()

    correct = 0
    for i, word in enumerate(current_word_list, 1):
        print(f"\nWord {i}/{wordNumbers}: {word}\n")
        if input("Type the word: ") == word:
            print("Correct!")
            correct += 1
        else:
            print("Incorrect!")

    print("\nTest over.")
    print(f"Score: {correct}/{wordNumbers} ({correct/wordNumbers:.0%})")
    if timeTest:
        print(f"Time: {time.time()-start_time:.2f}s")

# Main game loop
while True:
    run_test()
    
    while True:
        print("\nOptions:")
        print("1. Repeat same test")
        print("2. New test")
        print("3. Exit")
        choice = input("Choose (1-3): ").strip()
        print(choice)
        
        if choice == "1":
            word_list = get_words_from_file()
        elif choice == "2":
            word_list = get_words_manually()
        elif choice == "3"
            quit()
        else:
            print("Invalid choice, defaulting to manual entry.")
            word_list = get_words_manually()
