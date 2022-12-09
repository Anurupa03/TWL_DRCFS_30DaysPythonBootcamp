
# constants
SCISSOR = "scissor"
ROCK = "rock"
PAPER = "paper"

# tuple of options
game_choice = (ROCK,PAPER,SCISSOR)


player1_name = input("Enter player 1 name: ")
player2_name = input("Enter player 2 name: ")


player1_score = 0
player2_score = 0

for i in range(5):
    player1_choice = input(f'{player1_name} : rock, paper or scissor ? ')
    player2_choice = input(f'{player2_name} : rock, paper or  scissor? ')


    if player1_choice == player2_choice:
        pass
    elif player1_choice == ROCK:
        if player2_choice == SCISSOR:
            player1_score += 1
        else:
            player2_score += 1
    elif player1_choice == SCISSOR:
        if player2_choice == PAPER:
            player1_score += 1
        else:
            player2_score += 1
    elif player1_choice == PAPER: 
        if player2_choice == ROCK:
            player1_score += 1
            print(player1_score)
        else:
            player2_score += 1
    else:
        print("Invalid play")
    

print(f'{player1_name} score is : {player1_score}')
print(f'{player2_name} score is : {player2_score}')
if player1_score == player2_score:
    print("Draw")
elif player1_score > player2_score:
    print(f'{player1_name} wins')
else:
    print(f'{player2_name} wins')

