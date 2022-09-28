import random
turns = ['rock', 'paper', 'scissors']
human_turns = []
computer_turns = []
draw_history = []
win_history = []
loss_history = []


while(True):
    human_turn = input("Enter your turn, or type exit: ")
    computer_turn = random.choice(turns)

    if human_turn == 'exit':
        print('Thank you for playing! Bye bye')
        break

    human_turns.append(human_turn)
    computer_turns.append(computer_turn)

    print(f'Human:{human_turn} vs. Computer:{computer_turn}')
    if human_turn == computer_turn:
        print('Draw!')
        draw_history.append('Draw!')
    elif human_turn == 'rock' and computer_turn == 'scissors':
        print('Human wins!')
        win_history.append('Win!')
    elif human_turn == 'paper' and computer_turn == 'rock':
        print('Human wins!')
        win_history.append('Win!')
    elif human_turn == 'scissors' and computer_turn == 'paper':
        print('Human wins!')
        win_history.append('Win!')
    else:
        print('Computer wins!')
        loss_history.append('Loss!')

print(f'You have played {len(human_turns)} times!')
print(f'You have won {len(win_history)} times!')
print(f'You picked the same thing as the computer {len(draw_history)} times!')
print(f'You have lost {len(loss_history)} times!')
