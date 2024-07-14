import time
from random import choice

# Sample data
teams = {
    'TeamA': ['PlayerA1', 'PlayerA2', 'PlayerA3', 'PlayerA4', 'PlayerA5', 'PlayerA6', 'PlayerA7', 'PlayerA8', 'PlayerA9', 'PlayerA10', 'PlayerA11'],
    'TeamB': ['PlayerB1', 'PlayerB2', 'PlayerB3', 'PlayerB4', 'PlayerB5', 'PlayerB6', 'PlayerB7', 'PlayerB8', 'PlayerB9', 'PlayerB10', 'PlayerB11']
}

batBall = ['BAT', 'BOWL']
balls = [0, 1, 2, 4, 6, 'OUT']
out = ['Caught!', 'Bowled!', 'Run Out!']

# Function to handle toss and first choice
def toss_time(team1, team2):
    print(f'{team1} won the toss. What would you like to do? Bat or Bowl?')
    call = input('').upper()
    while call not in batBall:
        print('Type correctly!!')
        call = input('').upper()
    print(f'{team1} chose to {call} first')
    if call == 'BAT':
        batting_team, bowling_team = team1, team2
    else:
        batting_team, bowling_team = team2, team1
    return batting_team, bowling_team

# Function to play the innings
def innings(batting_team, bowling_team, first_scores):
    batting_team_list = teams[batting_team]
    batting_options = iter(batting_team_list)
    on_strike = next(batting_options)
    on_strike_scores = []
    player_scores = []
    wickets = 10
    total = []
    team_total = 0
    bowling_options = teams[bowling_team][5:]

    for over in range(3):
        bowler = choice(bowling_options)
        print(f'{on_strike} is on strike, {bowler} is bowling.')
        for ball in range(1, 7):
            ball_delivered = choice(balls)
            if wickets == 0 or team_total > first_scores:
                break
            elif ball_delivered == 'OUT':
                print(f'{over}.{ball} LBW !!! {bowler} has taken the wicket of {on_strike}')
                player_scores = sum(on_strike_scores)
                team_total = sum(total)
                out_player_scores = {on_strike: player_scores}
                print(f'{batting_team} is at {team_total}')
                print(out_player_scores)
                on_strike = next(batting_options)
                wickets -= 1
                on_strike_scores = []
                time.sleep(2)
            else:
                print(f'{over}.{ball}', end='')
                start = time.time()
                input('')
                end = time.time()
                time_taken = end - start
                if time_taken < 1:
                    print('A sixxxxerrrr!!')
                    total.append(6)
                    on_strike_scores.append(6)
                elif 1 <= time_taken < 1.5:
                    print('Boundaryyy!!!')
                    total.append(4)
                    on_strike_scores.append(4)
                elif 2 <= time_taken < 2.5:
                    print('only 2 runs')
                    total.append(2)
                    on_strike_scores.append(2)
                elif 2.5 <= time_taken < 3:
                    print(f'{on_strike} duck the ball')
                    total.append(0)
                    on_strike_scores.append(0)
                else:
                    print(f'{choice(out)} {bowler} has taken the wicket of {on_strike}')
                    player_scores = sum(on_strike_scores)
                    team_total = sum(total)
                    out_player_scores = {on_strike: player_scores}
                    print(f'{batting_team} is at {team_total}')
                    print(out_player_scores)
                    on_strike = next(batting_options)
                    wickets -= 1
                    on_strike_scores = []
            team_total = sum(total)
            print(f'{batting_team} is at {team_total}')
            print(f'{on_strike} is at {sum(on_strike_scores)}\n')
    return team_total

# Initialize teams and call
firstTeam = 'TeamA'
secondTeam = 'TeamB'
tossCall = ['TeamA', 'TeamB']
toss = choice(tossCall)

# Main game logic
if toss == tossCall[0]:
    batting_team, bowling_team = toss_time(firstTeam, secondTeam)
    first_innings_total = innings(batting_team, bowling_team, 1000)
    print(f'{bowling_team} needs {first_innings_total} runs to win the match')
    second_innings_total = innings(bowling_team, batting_team, first_innings_total)
    if first_innings_total > second_innings_total:
        print(f'{batting_team} has won the match')
    elif second_innings_total > first_innings_total:
        print(f'{bowling_team} has won the match')
    else:
        print('Draw! Both teams scored the same runs')

else:
    batting_team, bowling_team = toss_time(secondTeam, firstTeam)
    first_innings_total = innings(batting_team, bowling_team, 1000)
    print(f'{bowling_team} needs {first_innings_total} runs to win the match')
    second_innings_total = innings(bowling_team, batting_team, first_innings_total)
    if first_innings_total > second_innings_total:
        print(f'{batting_team} has won the match')
    elif second_innings_total > first_innings_total:
        print(f'{bowling_team} has won the match')
    else:
        print('Draw! Both teams scored the same runs')

