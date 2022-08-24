import random
while True:
    def get_choices():
        """create choices for pc or human"""
        player_choice = input("Enter a choice (rock, paper, scissors): ")
        options = ["rock", "paper", "scissors"]
        computer_choice = random.choice(options)
    
        choices = {"player": player_choice, "computer": computer_choice}
        return choices

    def check_win(player, computer):
        """Determining the winner"""
        print(f"You chose {player}, Computer chose {computer}")
        if player == computer:
            return "Its a tie"
        elif player == "rock":
            if computer == "scissors":
                return "Rock smashes scissors. You win! "
            else:
                return "Paper covers rock. You loose:-( "
        elif player == "paper":
            if computer == "rock":
                return "Paper covers rock. You win! "
            else:
                return "Scissors cuts paper. You loose:-( "
        elif player == "scissors":
            if computer == "paper":
                return "Scissors cuts paper. You win! "
            else:
                return "Rock smashes scissors. You loose:-( "
            
    def score_system(data_store):
        """Create a score system to record results"""
        # Make an analysis of the results and display them
        # Check who has the highest scores.
        print("\nGame Results: ")
        if len(data_store["player"]) > len(data_store["computer"]):
            print("\t\nPlayer wins")
            print("Won by " + str(len(data_store["player"])) + " points")
        else: 
            print("\t\nComputer wins")
            print("Won by " + str(len(data_store["computer"])) + " points")
            
    # Storing results in a dictionary
    data_store = {}
    data_store['player'] = []
    data_store['computer'] = []
        
        
    choices = get_choices()
    result = check_win(choices["player"], choices["computer"])
    print(result)
    
    if 'You win' in result:
        data_store['player'].append(result)
    else:
        data_store['computer'].append(result)
        
    proceed = input("\nWould you like to proceed? (yes/no): ")
    if proceed == 'no':
        score_system(data_store)
        break
            
               