import random

random_choice = random.randint(0,2)

if random_choice == 0:
    comp_choice = 'rock'
elif random_choice == 1:
    comp_choice = 'paper'
else:
    comp_choice = 'scissors'

while True:
    
    user_choice = input ("Choose one of them: rock/paper/scissors ")
    while user_choice != 'rock' and user_choice != 'paper' and user_choice !='scissors':
     user_choice = input("Your value is not valid. Please choose correct option (rock/paper/scissors): ")


    if comp_choice == user_choice:
        winner = 'Tie'
    elif comp_choice == 'paper' and user_choice == 'rock':
        winner = 'Computer'
    elif comp_choice == 'rock' and user_choice == 'scissors':
        winner = 'Computer'
    elif comp_choice == 'scissors' and user_choice == 'paper':
        winner = 'Computer'
    else:
        winner = 'User'


    if winner == 'Tie':
        print ("No winner. Play again!")
    else:
        print('The', winner, 'won! The computer choice was', comp_choice, '.')
    
    

