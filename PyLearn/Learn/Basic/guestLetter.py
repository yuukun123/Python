def guestLetter():
    print("Welcome to Hangman!")
    strings = "Fish"
    chance = 5
    char = ["_" for _ in strings]
    print("".join(char))
    while chance > 0:
        letter = input("\nEnter a letter: ")
        if letter in strings.lower():
            for i in range(len(strings)):
                if strings[i].lower() == letter and char[i] == "_":
                    char[i] = letter
            print("".join(char))
        else:
            chance -= 1
            print("You guessed a wrong letter!")
            print(f"You have {chance} chances left!")

        if "_" not in char:
            print("You win!")
            break

    if "_" in char:
        print("You lose!")

guestLetter()
