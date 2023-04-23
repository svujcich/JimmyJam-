import random


# yes or no
def valid_choice(choice):
    while True:
        # choice = input("> ").upper().strip()
        if (choice == "Y") or (choice == "N"):
            return choice

        if (choice != "Y") or (choice != "N"):
            print("Try again with a valid selection! (Y / N)")
            choice = input("> ").upper().strip()


# # pick a random word for hangman
keywords = ["AUTUMN", "PUMPERNICKEL", "DUSTBUNNY", "PICKELFORK", "SWIMSUIT"]
selection = random.randint(0, len(keywords) - 1)
keyword = keywords[selection]

correct_guesses = []
wrong_guesses = []

letter_1 = ""
letter_2 = ""
letter_3 = ""
letter_4 = ""
letter_5 = ""
letter_6 = ""
letter_7 = ""
letter_8 = ""
letter_9 = ""
letter_10 = ""
letter_11 = ""
letter_12 = ""

correct_letters = [
    letter_1,
    letter_2,
    letter_3,
    letter_4,
    letter_5,
    letter_6,
    letter_7,
    letter_8,
    letter_9,
    letter_10,
    letter_11,
    letter_12,
]

# assign an _ for each letter in the keyword
i = 0

num_letters = len(keyword)
while i < num_letters:
    correct_letters[i] = "_ "
    i += 1

# correct_letters[0] = "A "
# correct_letters[1] = "B "
# correct_letters[2] = "C "
# correct_letters[3] = "C "

# print(correct_letters[0], correct_letters[1], correct_letters[2], correct_letters[3],\
#      correct_letters[4], correct_letters[5], correct_letters[6], correct_letters[7],\
#      correct_letters[8], correct_letters[9], correct_letters[10], correct_letters[11])
# print(keyword)

# print(len(wrong_guesses))
# print(type(len(wrong_guesses)))


def setup_board():
    guess_count = len(wrong_guesses)
    if guess_count == 0:
        print("---------")
        print("| /")
        print("|/")
        print("|")
        print("|")
        print("_ " * len(keyword))

    elif guess_count == 1:
        print("---------")
        print("| /     O")
        print("|/")
        print("|")
        print("|")
        print("_ " * len(keyword))

    elif guess_count == 2:
        print("---------")
        print("| /     O")
        print("|/      |")
        print("|")
        print("|")
        print("_ " * len(keyword))

    elif guess_count == 3:
        print("---------")
        print("| /     O")
        print("|/      |\\")
        print("|")
        print("|")
        print("_ " * len(keyword))

    elif guess_count == 4:
        print("---------")
        print("| /     O")
        print("|/     /|\\")
        print("|")
        print("|")
        print("_ " * len(keyword))

    elif guess_count == 5:
        print("---------")
        print("| /     O")
        print("|/     /|\\")
        print("|        \\")
        print("|")
        print("_ " * len(keyword))

    elif guess_count == 6:
        print("---------")
        print("| /     O")
        print("|/     /|\\")
        print("|      / \\")
        print("|")
        print("_ " * len(keyword))


# setup_board()

guess = "G"


def add_letters(guess):
    if guess in keyword:
        for i, letter in enumerate(keyword):
            if letter == guess:

                if letter not in correct_guesses:
                    correct_guesses.append(letter)
                    return (i, letter)
    else:
        print(f"{guess} is NOT in {keyword}")
        wrong_guesses.append(guess)

        # answer = add_letters(guess)


# print(answer)
# print(correct_guesses)
# print(wrong_guesses)

# test = ["this", "that"]

# print(test[0] + test[1])


#------------------
# PLAY THE GAME
def jimmyjam():
    while True:
        # intro
        print("Welcome to JIMMYJAM")
        print("------------------")
        print("At a royal party, Jimmy accidentally spilled wine on the King and embarrassed him, so Jimmy’s punishment is death. Jimmy would like your help to persuade the King to let him off with a warning.")
        print()
        print("Are you willing to help Jimmy? (Y / N)")
        choice = input("> ").upper().strip()
        # funnel choice through function to catch incorrect entries
        choice = valid_choice(choice)

        if choice == "N":
            break

        print()
        print("Great!")

        # capture username
        print("What can I call you?")
        username = input("> ").upper().strip()
        print()

        print(f"Oh, so you're {username}! Jimmy said you were best friends growing up")
        print("I've only heard good things about you!")
        print("Great to meet you!")
        print()
        print("Here's how you can help jimmy...")
        break


jimmyjam()

print("GAME OVER")

        
        
        
        
    
    

               

        
    
    
    
    
    



