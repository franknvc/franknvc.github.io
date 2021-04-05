import os, random

os.system("cls")

# Initialize
hangman = ["""
           _______
           |     
           |    
           |    
           |
           |
           |__________""",
           """
           _______
           |     |
           |    
           |    
           |
           |
           |__________""",
           """
           _______
           |     |
           |     O
           |
           |
           |
           |
           |__________""",
           """
           _______
           |     |
           |     O
           |     |
           |     |
           |
           |
           |__________""",
           """
           _______
           |     |
           |     O
           |    \\|/
           |     |
           |
           |
           |__________""",
           """
           _______
           |     |
           |     O
           |    \\|/
           |     |
           |    / \\
           |
           |__________""",
           """
           _______
           |     |
           |     O
           |    /|\\
           |     |
           |    | |
           |
           |__________""",
           """
                 O
                \\|/
               \\\\|
           __________    
           """]

words = ["ZEBRA", "MANJARO", "TESLA", "PYTHON"]
word = random.choice(words)
guess = "-" * len(word)
wrong_letters = ""

# Print header
print("HANGMAN\n")
print(hangman[0])

# Main game loop
while True:
    print(f"Current guess: {guess}")
    print(f"Wrong guesses: {wrong_letters}")

    letter = input("Please enter a letter. > ").upper()[0]

    # check if the letter is in the word
    if letter in word:
        temp = ""
        for index in range(len(word)):
            if letter == word[index]:
                temp += letter
            elif guess[index] != '-':
                temp += guess[index]
            else:
                temp += '-'
        guess = temp
    else:
        wrong_letters += letter

    # Check for a winner
    if word == guess:
        print("You win! And you live to play another day!")
        print(hangman[len(hangman) - 1])
        exit()

    print(hangman[len(wrong_letters)])

    if len(wrong_letters) == 6:
        print("You lose!")
        print(f"The word was {word}")
        exit()
