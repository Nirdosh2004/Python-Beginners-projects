# import random

# def roll():
#           min_value = 1
#           max_value = 6
#           roll = random.randint(min_value,max_value)

#           return roll
# while True:
#           players = input("Enter the number of players (1-4) : ")
#           if players.isdigit():
#                   players = int(players)
#                   if 1 <=  players <= 4:
#                           break
#                   else:
#                           print("Must be between 2 - 4 players. ")
#           else:
#                     print("Invalid! Try Again")
                          
# max_score = 50
# player_scores = [0 for _ in range(players)]

# while max(player_scores) < max_score:
        
#         for player_idx in range(players):
                
#         current_score = 0

#         should_roll = input("would you like to roll(y) : ")
#         if should_roll.lower() != "y":
#                 break
#         value = roll()
#         if value == 1:
#                 print("You rolled a 1! Turn down!")
#         else:
#                 current_score += value
#                 print("You rolled a :" , value)
        
#         print("Your current score is " , current_score)