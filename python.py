import random
import math


def best_of(n):
    if n % 2 == 0:
        return int(n/2)+1
    else:
        return math.ceil(n/2)

def rps():
    cpu_selection = ['rock', 'paper', 'scissors']
    cpu_wins = 0
    player_wins = 0
    best_of_games = False
    application_running = False
    while True:
        multiplayer_input = input("\nBefore we begin, would you like to play multiplayer? Enter Yes / No : ")
        if multiplayer_input.lower() == "yes":
            multiplayer_rps()
            return
        elif multiplayer_input.lower() == "no":
            break
        else:
            print("Not a valid input, try again")
    while True:
        best_of_option = input("\nWelcome to Rock Paper Scissors, do you want to play Best of games? (Bo3, Bo5, etc.) Enter Yes / No : ")
        if best_of_option.lower() == "yes":
            best_of_games = True
            application_running = True
            while True:
                number_of_games = input("\nPlease enter a number for the best of games (5 would be Best of 5): ")
                if number_of_games.isdigit() and int(number_of_games) >= 0:
                    break            
                else:
                    print("Not a valid input, try again")
            winning_number = best_of(int(number_of_games))
            print(f"Games needed to win: {winning_number}")
            break
        elif best_of_option.lower() == "no":
            application_running = True
            break
        else:
            print("Not a valid input, try again")
    while application_running == True:
        if best_of_games == True:
            if player_wins == winning_number:
                print(f"Horray! Lets go Champ! You're the winner! You scored {winning_number} out of {number_of_games}")
                break
            if cpu_wins == winning_number:
                print(f"Sorry, but you lost this best of {number_of_games}")
                break
        cpu_choice = random.choice(cpu_selection)
        user_input = input("\nPlease enter Rock, Paper, or Scissors to play, 'Q' to quit: ")
        #Begin checking who wins
        if user_input.lower() == cpu_choice:
            print(f"This game was a tie, you both chose {cpu_choice}")
            print(f"Player score - {player_wins} Computer score - {cpu_wins}")
        elif user_input.lower() == "rock" and cpu_choice == 'scissors':
            print("Rock beats scissors. You win this round!")
            player_wins += 1
            print(f"Player score - {player_wins} Computer score - {cpu_wins}")
        elif user_input.lower() == "rock" and cpu_choice == 'paper':
            print("Paper beats rocks. You lost this round!")
            cpu_wins += 1
            print(f"Player score - {player_wins} Computer score - {cpu_wins}")
        elif user_input.lower() == "paper" and cpu_choice == 'scissors':
            print("Scissors beats paper. You lost this round!")
            cpu_wins += 1
            print(f"Player score - {player_wins} Computer score - {cpu_wins}")
        elif user_input.lower() == "paper" and cpu_choice == 'rock':
            player_wins += 1
            print("Paper beats rock. You win this round!")
            print(f"Player score - {player_wins} Computer score - {cpu_wins}")
        elif user_input.lower() == "scissors" and cpu_choice == 'paper':
            print("Scissors beats paper. You win this round!")
            player_wins += 1
            print(f"Player score - {player_wins} Computer score - {cpu_wins}")
        elif user_input.lower() == "scissors" and cpu_choice == 'rock':
            print("Rock beats scissors. You lost this round!")
            cpu_wins += 1
            print(f"Player score - {player_wins} Computer score - {cpu_wins}")
        elif user_input.lower() == 'q':
            if player_wins > cpu_wins:
                print(
                    f"You won {player_wins} times, the cpu won {cpu_wins} times, You win the game!")
            elif player_wins < cpu_wins:
                print(
                    f"You won {player_wins} times, the cpu won {cpu_wins} times, You lost the game!")
            else:
                print(
                    f"You won {player_wins} times, the cpu won {cpu_wins} times, You tied the game!")
            break
        else:
            print("This is not a valid choice, please try again.")



def multiplayer_rps():
    
    def printScore():
            print(f"\nHere is the current score:\nYou have {player_wins} wins")
            for key, value in cpu_names.items():
                print(f"{key} has {value} wins")
    
    while True:
        number_of_opp = input("\nPlease enter the number of opponents you would like: ")
        if number_of_opp.isdigit() and int(number_of_opp) >= 0:
            break            
        else:
            print("Not a valid input, try again")
    cpu_names = {}
    for n in range(int(number_of_opp)):
        cpu_name = input(f"\nEnter Player {n}'s name: ")
        cpu_names[cpu_name.title()] = 0
    player_wins = 0
    best_of_games = False
    application_running = False
    cpu_selection = ['rock', 'paper', 'scissors']
    
    while True:
        best_of_option = input("\nWelcome to Rock Paper Scissors MULTIPLAYER, do you want to play Best of games? (Bo3, Bo5, etc.) Enter Yes / No : ")
        if best_of_option.lower() == "yes":
            best_of_games = True
            application_running = True
            while True:
                number_of_games = input("\nPlease enter a number for the best of games (5 would be Best of 5): ")
                if number_of_games.isdigit() and int(number_of_games) >= 0:
                    break            
                else:
                    print("Not a valid input, try again")
            winning_number = best_of(int(number_of_games))
            print(f"Games needed to win: {winning_number}")
            break
        elif best_of_option.lower() == "no":
            application_running = True
            break
        else:
            print("Not a valid input, try again")    
    
    while application_running == True:
        #best of: calculating if the game is over
        if best_of_games == True:
            if winning_number in cpu_names.values() or player_wins == winning_number:
                print(f"The game has ended! These are the winners:")
                if player_wins == winning_number:
                    print(f"YOU")
                for key, val in cpu_names.items():
                    if val == winning_number:
                        print(f"{key}")
                return
        cpu_choices = []
        for x in cpu_names:
            cpu_choices.append(random.choice(cpu_selection))
        user_input = input("\n \nPlease enter Rock, Paper, or Scissors to play, 'Q' to quit: ")
        if user_input.lower() == "rock" or user_input == "paper" or user_input == "scissors":
            for name, choice in zip(cpu_names.keys(), cpu_choices):
                print(f"{name} has chosen {choice}")

        cpu_choices.append(user_input)
        #Begin checking who wins
        if user_input.lower() == "rock" or user_input.lower() == "paper" or user_input.lower() == "scissors" or user_input.lower() == "q":
            if "rock" in cpu_choices and "paper" in cpu_choices and "scissors" in cpu_choices and user_input.lower() != "q":
                print(f"This game is a tie, so nobody scores!")
                printScore()
            elif all(x == "rock" for x in cpu_choices) and user_input.lower() != "q": 
                print(f"This game is a tie, so nobody scores!")
                printScore()
            elif all(x == "paper" for x in cpu_choices) and user_input.lower() != "q": 
                print(f"This game is a tie, so nobody scores!")
                printScore()
            elif all(x == "scissors" for x in cpu_choices) and user_input.lower() != "q": 
                print(f"This game is a tie, so nobody scores!")
                printScore()
            elif "rock" in cpu_choices and "scissors" in cpu_choices and "paper" not in cpu_choices and user_input.lower() != "q":
                cpu_choices.pop()
                for ind, v in zip(cpu_names.keys(), cpu_choices):
                    if v == "rock":
                        print(f"{ind} scored a point!")
                        cpu_names[ind] += 1
                if user_input == "rock":
                        print(f"You scored a point!")
                        player_wins += 1
                printScore() 
            elif "paper" in cpu_choices and "scissors" in cpu_choices and "rock" not in cpu_choices and user_input.lower() != "q":
                cpu_choices.pop()
                for ind, v in zip(cpu_names.keys(), cpu_choices):
                    if v == "scissors":
                        print(f"{ind} scored a point!")
                        cpu_names[ind] += 1
                if user_input == "scissors":
                        print(f"You scored a point!")
                        player_wins += 1
                printScore()
            elif "rock" in cpu_choices and "paper" in cpu_choices and "scissors" not in cpu_choices and user_input.lower() != "q":
                cpu_choices.pop()
                for ind, v in zip(cpu_names.keys(), cpu_choices):
                    if v == "paper":
                        print(f"{ind} scored a point!")
                        cpu_names[ind] += 1
                if user_input == "paper":
                        print(f"You scored a point!")
                        player_wins += 1 
                printScore()       
            elif user_input.lower() == "q":
                print(f"The game has ended! Here are the final scores:")
                for key, value in cpu_names.items():
                    print(f"{key} had {value} wins")
                print(f"You had {player_wins} wins")
                return
        else:
                print("This is not a valid choice, please try again.")    
        





rps()