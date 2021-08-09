# 단어를 랩덤을 뺴오기
import random
from hang import hang
#  단어가 하나만 그리고 다른 스펠링만 들어오게 체크
def analyize_word():
    while True:
        global typing_word
        typing_word = input('Input one letter: ')
        if typing_word in lst_typing:
            print('이미 입력한 단어 입니다. 다시 입력하세요 ')
            print(f'Left chance : {10 - chance}')
            continue
        if len(typing_word) != 1:
            print('한 글자만 입력하시오')
            print(f'Left chance : {10 - chance}')
        else:
            break
# 행맨 그림
def hang():
    if typing_word not in word:
        if chance == 1:
            print('''
                     ___
                    |   |______
                    |          |
                    |__________|
                    ''')
        elif chance == 2:
            print('''
                      |
                      |
                      |
                      |
                      |
                     _|_
                    |   |______
                    |          |
                    |__________|''')
        elif chance ==3:
            print('''
                      |-----
                      |
                      |
                      |
                      |
                     _|_
                    |   |______
                    |          |
                    |__________|''')

        elif chance == 4:
            print('''
              |-----
              |    |
              |    |
              |
              |
             _|_
            |   |______
            |          |
            |__________|''')
        elif chance == 5:
            print('''
              |-----
              |    |
              |    |
              |    O
              |
             _|_
            |   |______
            |          |
            |__________|''')
        elif chance == 6:
            print('''
              |-----
              |    |
              |    |
              |    O
              |    |
             _|_
            |   |______
            |          |
            |__________|''')
        elif chance == 7 :
            print('''
              |-----
              |    |
              |    |
              |    O
              |   /| 
             _|_
            |   |______
            |          |
            |__________|''')
        elif chance == 8 :
            print('''
              |-----
              |    |
              |    |
              |    O
              |   /|\ 
             _|_
            |   |______
            |          |
            |__________|''')
        elif chance == 9 :
            print('''
              |-----
              |    |
              |    |
              |    O
              |   /|\ 
             _|_  /
            |   |______
            |          |
            |__________|''')
        elif chance == 10:
            print('''
              |-----
              |    |
              |    |
              |    O
              |   /|\ 
             _|_  / \\
            |   |______
            |          |
            |__________|''')
# word 와 typing_word 를 비교하며 split 으로 나눈 blank 에 인덱스로 채워넣고, 다시 join 으로 봉합해줌
def split_join():
    global blank_word
    for idx in range(len(word)):
        blank_word = list(blank_word)
        if typing_word == word[idx]:
            blank_word[idx] = typing_word
            blank_word = ''.join(blank_word)

        else:
            blank_word = ''.join(blank_word)

# 만약 입력한 스펠링이 처음 입력하는거면 lst_typing 에 저장
def save_lst_typing():
    if typing_word not in lst_typing:
        lst_typing.append(typing_word)
    else:
        pass
# 맞으면 축하 아니면 안 축하
def congratulation():
    if blank_word == word:
        print(f'You correct the word ,chance left: {10 - chance}')
    else:
        # 단어 알려주기
        print(f'The word : ', word)
        print('You didnt correct the word')

# words.txt에서 랜덤 단어를 가져옴
with open('words.txt', 'r') as f:
    all_txt = f.read()
    split_txt = all_txt.split()
word = random.sample(split_txt, k=1)
word = ''.join(word)
chance = 0
# 빈칸을 만들어서 typing_word 가 맞으면 하나 씩 채워 넣기
blank_word = '_' * len(word)
lst_typing = []
# 기회 10번 소모하면 게임 끝
while chance != 10:
    #  단어가 하나만 그리고 다른 스펠링만 들어오게 체크
    analyize_word()
    # 만약 입력한 스펠링이 처음 입력하는거면 lst_typing 에 저장
    save_lst_typing()
    # 맞고 틀리고 구분
    split_join()
    # Typing word가 아니면 기회 하나씩 날아감
    if typing_word not in word:
        chance += 1
    # 행맨 그림 보여줌
    hang()
    # 채워넣은 단어와, 남은 챈스를 보여줌, 맞추면 탈출
    print(blank_word)
    print(f'Left chance : {10 - chance}')
    if blank_word == word:
        break
# 맞추면 축하 아님 안 축하
congratulation()
