"""
project_2.py: druhý projekt do Engeto Online Python Akademie

author: Václav Zmuda
email: vaclav.zmuda@gmail.com
discord: vaclav5301
"""

import random


# Generování náhodného čísla
def create_number():
    while True:
        cislice = random.sample(range(0, 10), 4) 
        if cislice[0] != 0:  # Zkontroluje, zda první číslice není nula
            return str(''.join(map(str, cislice))) 

# Kontrola složení
def num_check(x):
    for char in x:
        if char.isnumeric() != True:
            return False


# Kontrola tipu
def tip_check(tip):

    if num_check(tip) == False:
        print("You can only enter numbers")
        tip = input("Enter a new number: ")
        tip_check(tip)
    elif len(tip) != 4:
        print("Your number is too short or too long")
        tip = input("Enter a new number: ")
        tip_check(tip)
    elif tip[0] == "0":
        print("Your number cannot start with 0")
        tip = input("Enter a new number: ")
        tip_check(tip)
        
    for index, i in enumerate(tip):
        index += 1
        if i in tip[(index):4] and index < 4:
             print("Your number has duplicity in digits")
             tip = input("Enter a new number: ")
             tip_check(tip)


    return tip


# Porovnání tipu se správnou odpovědí
def compare(tip, answer):
    index, bulls, cows = 0, 0, 0
    for num in tip:
        if num == answer[index]:
            bulls += 1
            index += 1
        elif num in answer:
            cows += 1
            index += 1
        else:
            index += 1
    result(bulls,cows)
        
def result(bulls, cows):
    if bulls < 2 and cows < 2:
        print(f"{bulls} bull, {cows} cow")
    elif bulls < 2 and cows >= 2:
        print(f"{bulls} bull, {cows} cows")
    elif bulls >= 2 and cows < 2:
        print(f"{bulls} bulls, {cows} cow")
    else:
        print(f"{bulls} bulls, {cows} cows")

def main():
    separator = "-" * 60
  
    # Uvítání  
    print(f"""Hi there!
{separator}
I've generated a random 4 digit number for you.
Let's play a bulls & cows game!
Write HELPME to show the number or EXIT for exit the program

{separator}""")


    # Hádání
    while True:
        answer = create_number()
        guesses = 0
        while True:
            tip = input("Enter a number: ").upper()
            if tip == "HELPME":
                print(f"The answer is {answer}. You lost! :(")
                break
            elif tip == "EXIT":
                exit()
            else:
                tip = tip_check(tip)
                compare(tip, answer)
                print(separator)
                guesses += 1
                if tip == answer:
                    print(f"""Correct! You have guessed the right number 
                        in {guesses} guesses! """)
                    break

if __name__ == "__main__":
    main()
