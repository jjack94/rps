# weapon reset var to check if weapon is selected
reset_weapon = False

# variables for scores that defaults to 0
score_cpu = 0
score_user = 0
score_tie = 0

# vars for options for user
rock = "r", "R", "rock", "ROCK"
paper = "p", "paper"
scissors = "s", "scissors"

cpu_weapons: ["rock", "paper", "scissors"]

# vars for player and cpu players to hold their weapon choices that defaults as rock
# this allows users to stay with rock if they choose to, which is close to real game with only using neutral
# starting position of rock which is r
user_weapon = ""
cpu_weapon = ""

# vars to track how many times each weapon is used
rock_used = 0
paper_used = 0
scissors_used = 0

# cpu weapons tracking
cpu_rock_used = 0
cpu_paper_used = 0
cpu_scissors_used = 0

# keep playing game var
play_cont = "y"
