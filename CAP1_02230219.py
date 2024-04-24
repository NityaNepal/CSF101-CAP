# Nitya Nepal
# 1ICE
# 02230219
#################################
# REFERENCES
# Links that you referred while solving 
# the problem
# http://link.to.an.article/video.com 
################################
# SOLUTION
# Your Solution Score:50267
# 9
#https://github.com/NityaNepal/CAP1.git
################################
# Read the input.txt file
def accumulate_scores(file_name):
    total_points = 0
    with open(file_name, 'r') as file:
        for line in file:
            opponent_move, goal = line.strip().split()
            round_points = compute_score(opponent_move, goal)
            total_points += round_points
    return total_points

def compute_score(opponent_move, goal):
    move_values = {'A': 1, 'B': 2, 'C': 3}
    if goal == 'X': # Aim to lose
        if opponent_move == 'A':
            your_move = 'C' # Choose Scissors
        elif opponent_move == 'B':
            your_move = 'A' # Choose Rock
        else:
            your_move = 'B' # Choose Paper
    elif goal == 'Y': # Aim to draw
        your_move = opponent_move # Match opponent's move
    else: # Aim to win
        if opponent_move == 'A':
            your_move = 'B' # Choose Paper
        elif opponent_move == 'B':
            your_move = 'C' # Choose Scissors
        else:
            your_move = 'A' # Choose Rock

    base_points = move_values[your_move]
    if goal == 'X':
        base_points += 0
    elif goal == 'Y':
        base_points += 3
    else:
        base_points += 6

    return base_points

input_file = r"CSF101-CAP/input_9_cap1.txt"
total_points = accumulate_scores(input_file)
print(f'Total points: {total_points}')