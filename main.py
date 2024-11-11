import random

def play():
    choices = ['rock', 'paper', 'scissors']

    while True:
        print('\nRock, Paper, Scissors')
        print('Enter your choice: (rock, paper, scissors)')
        play_choice = input().lower()

        if play_choice not in choices:
            print('Invalid choice! Please choose again.')
            continue

        computer_choice = random.choice(choices)
        print(f'\nYou: {play_choice}.')
        print(f'Computer: {computer_choice}.\n')

        print(winner(play_choice, computer_choice))

        play_again = input('Do you want to play again? (y/n): ').lower()

        if play_again != 'y':
            print('Thanks for playing!\n')
            break

def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors' or
          user_choice == 'paper' and computer_choice == 'rock' or
          user_choice == 'scissors' and computer_choice == 'paper'):
        return 'You Win!'
    else:
        return 'Computer Wins!'

if __name__ == '__main__':
    play()
