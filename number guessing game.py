#guessing number
import pyfiglet
banner = pyfiglet.figlet_format("Welcome to Number guessing game!!")
print(banner)
def game():
    
    import random
    numbers = []
    num = 1
    while num <=100:
        numbers.append(num)
        num += 1

#print(numbers)
    guess_number = random.choice(numbers)
#print(guess_number)

    level = input("whether you want to play a easy or hard level").lower()
    n=10
    m=5
    while level == 'easy':
        if n>0:
            user_guess = int(input("enter your guess."))
            if guess_number == user_guess:
                print("you won")
            elif guess_number > user_guess:
                print("too low")
            elif guess_number< user_guess:
                print("too high")
            n-=1
            print(f"you are left with {n} guesses.")

        else:
            print("you are out of guesses")
            exit()

    while level == 'hard':
        if m > 0:
            user_guess = int(input("enter your guess."))
            if guess_number == user_guess:
                print("you won")
            elif guess_number > user_guess:
                print("too low")
            elif guess_number < user_guess:
                print("too high")
            m -= 1
            print(f"you are left {m} guesses.  ")

        else:
            print("you are out of guesses")
            exit()

to_play = True
while to_play:
    play = input("do you want to play this game.\n type 'y' for yes and 'n' for no?").lower()
    if play == 'y':
        game()

    elif play == 'n':
        exit()


