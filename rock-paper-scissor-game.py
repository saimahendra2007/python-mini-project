import pyfiglet
ascii_banner = pyfiglet.figlet_format("Rock Paper Scissors")
print(ascii_banner)


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random


def rockpaperscissor():

    user = int(input("𝚠𝚑𝚊𝚝 𝚍𝚘 𝚢𝚘𝚞 𝚌𝚑𝚘𝚒𝚌𝚎? 𝚎𝚗𝚝𝚎𝚛 0 𝚏𝚘𝚛 𝚛𝚘𝚌𝚔, 1 𝚏𝚘𝚛 𝚙𝚊𝚙𝚎𝚛 𝚊𝚗𝚍 2 𝚏𝚘𝚛 𝚜𝚌𝚒𝚜𝚜𝚘𝚛."))
    computer_choice = random.randint(0, 2)
    if user == 0:
        print(rock)
    elif user == 1:
        print(paper)
    elif user == 2:
        print(scissors)
    else:
        print("enter the valid number")
    if computer_choice == 0:
        print(f"computer choice {computer_choice}", rock)
    elif computer_choice == 1:
        print(f"computer choice {computer_choice}", paper)
    elif computer_choice == 2:
        print(f"computer choice {computer_choice}", scissors)

    if user == 0 and computer_choice == 2:
        print("user won")
    elif user == 1 and computer_choice == 0:
        print("user won")
    elif user == 2 and computer_choice == 1:
        print("user won")
    elif user == computer_choice:
        print("match tie")
    else:
        print("you lost")

initial_game = True
continue_game = True

while initial_game:
    print("𝔀𝓮𝓵𝓬o𝓶𝓮 𝓽𝓸 𝓻𝓸𝓬𝓴 𝓹𝓪𝓹𝓮𝓻 𝓼𝓬𝓲𝓼𝓼𝓸𝓻 𝓰𝓪𝓶𝓮!!")
    user = input("Do you want to play this game?(yes/no)").lower()
    if user == 'yes':
        rockpaperscissor()
        while continue_game:
            user1 = input("do you want to play the game again?").lower()
            if user1 == 'yes':
                rockpaperscissor()
            elif user1 == 'no':
                continue_game = False
                initial_game = False
            else:
                print("enter a valid number.")

    else:
        initial_game = False


