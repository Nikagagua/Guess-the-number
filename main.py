import random
from art import logo

print(logo)


def welcome_message():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")


def random_number():
    ''' Declares the random number '''
    random_numbers = random.randint(1, 100)
    return random_numbers


random_number = random_number()


def make_guess():
    make_a_guess = int(input("Make a guess: "))
    return make_a_guess


def easy_difficulty(start):
    attempts = 10
    print(f"You have {attempts} attempts remaining to guess the number.")
    while attempts > 0:
        guess = make_guess()
        if guess == random_number:
            print(f"You got it! The answer was {random_number}.")
            return
        elif guess > random_number:
            print("Too high. Guess again.")
        else:
            print("Too low. Guess again.")
        attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number.")
    print(f"Game over! The number was {random_number}.")


def hard_difficulty(start):
    attempts = 5
    print(f"You have {attempts} attempts remaining to guess the number.")
    while attempts > 0:
        guess = make_guess()
        if guess == random_number:
            print(f"You got it! The answer was {random_number}.")
            return
        elif guess > random_number:
            print("Too high. Guess again.")
        else:
            print("Too low. Guess again.")
        attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number.")
    print(f"Game over! The number was {random_number}.")


is_game_over = True
start = welcome_message()
while True:
    choose_difficulty = input(
        "Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if choose_difficulty == "easy":
        easy_difficulty(start)
        break
    elif choose_difficulty == "hard":
        hard_difficulty(start)
        break
    else:
        print("Game is over! You could choose only between 'easy or 'hard'!")
        break
