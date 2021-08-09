import random

num_1 = 1
teams = []
# 팀명을 입력
while True:
    team = input(f'{num_1} 번쨰 (그만 입력하려면 \'Q\') : ')
    num_1 += 1
    if team == 'Q':
        break
    teams.append(team)

print(f'참가 팀들 : {teams}')
# 팀을 섞어줌
random.shuffle(teams)

# 대전 상대를 정해 줌 , 한 팀이 남을 때 까지
while len(teams) != 1:
    if len(teams) % 2 == 1:
        print(f'부전승 인 팀은 {teams[-1]} 입니다')
    # 부전승 하는 팀
    try:
        if len(teams) % 2 == 1 and won_by_default:
            teams.append(won_by_default)
        elif len(teams) % 2 == 1:
            won_by_default = teams[-1]
            del teams[-1]
    except:
        pass
    # 대전 상대를 정해줌
    tag = 1
    for x in range(0, len(teams)-1, 2):
        print(f'{tag}번쨰 매치 :[1]{teams[x]} vs [2]{teams[x+1]}')
        tag += 1
    # 승자를 입력하고
    for tag3 in range(len(teams)//2): # len(teams)/2 는 어떤 경우든 float 으로 나옴
        # 정확한 값 입력할떄까지 input
        while True:
            winner = input(f'{tag3+1}번쨰 경기 승자의 번호는 ? : ')
            if winner in ['1', '2']:
                break

        # 승자가 아니면 teams 에서 제거됨
        if winner == '1':
            del teams[tag3+1]
        elif winner == '2':
            del teams[tag3]


print(f'The winner is ===== {teams} ===== !!! Congratulation')