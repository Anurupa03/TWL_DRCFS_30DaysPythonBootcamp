player1_name = input("Enter player 1 name: ")
player2_name = input("Enter player 2 name: ")

player1_score = 0
player2_score = 0

for i in range(5):
    player1_choice = input(f'{player1_name} : rock, paper or scissor ? ')
    player2_choice = input(f'{player2_name} : rock, paper or  scissor? ')


    if player1_choice == player2_choice:
        pass
    elif player1_choice == "rock":
        if player2_choice == "scissors":
            player1_score = player1_score + 1
        else:
            player2_score = player2_score +1
    elif player1_choice == "scissors":
        if player2_choice == "paper":
            player1_score = player1_score + 1
        else:
            player2_score = player2_score +1
    elif player1_choice == "paper": 
        if player2_choice == "rock":
            player1_score = player1_score + 1
            print(player1_score)
        else:
            player2_score = player2_score +1
    

print(f'{player1_name} score is : {player1_score}')
print(f'{player2_name} score is : {player2_score}')
if player1_score == player2_score:
    print("Draw")
elif player1_score > player2_score:
    print(f'{player1_name} wins')
else:
    print(f'{player2_name} wins')

