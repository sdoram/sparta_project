import random
import time
import msvcrt
from script import *

def call_magician():
    # 몬스터가 랜덤으로 생성
    players = [2, 4, 5]
    # 플레이어 몇명인지 뽑기
    player = random.choice(players)

    str_1 = ['🍓', '🍌', '🍉', '🍏']  # 카드 모양 종류
    # card_amount = [5, 3, 3, 2, 1]  # 모양별 갯수(1개짜리 5개, 2개짜리 3개 ...)

    cards_tempt = []
    deck = []  # 전체 카드
    field = []  # 보여지는 카드
    dummy = []  # 이미 지나간 카드
    my_card = []  # 내가 가지고 있는 카드

    # 카드 구성하기
    for fruite in str_1:
        for num in range(1, 6):
            cards_tempt.append((fruite*num))

    for card in cards_tempt:
        if len(card) == 1:
            for i in range(1, 6):
                deck.append((card))
        elif len(card) == 2 or len(card) == 3:
            for i in range(1, 4):
                deck.append((card))
        elif len(card) == 4:
            for i in range(1, 3):
                deck.append((card))
        else:
            deck.append(card)

    # 카드 나눠주기 전에 섞기
    random.shuffle(deck)

    # 카드 몇장인지 정하기
    card_amount = 0

    if player == 2:
        card_amount = 28
    elif player == 4:
        card_amount = 14
    else:
        dummy.append(deck[0])
        deck.pop(0)
        card_amount = 11

    # 카드 나눠주기
    def devide_card(card, n):
        return [card[i: i+n] for i in range(0, len(card), n)]

    # [1,2,3,4,5,6,7,8] , 2

    # for i in rage(0, 8, 2)
    # [1,3,5,7]  1:1+2, 3:3+2, 5:5+2, 7:7+2
    # [2,4,6,8]  2:2+2, 4:4+2, 6:6+2, 8:8+2

    # range(시작, 끝, 숫자간격)

    # 카드 n빵
    devide_card_list = devide_card(deck, card_amount)

    # ~3초 안의 랜덤한 시간 뿌리기

    def ran_time():
        return round(random.random()*random.randint(1, 3), 2)

    # 각자 카드 갖기
    my_card = devide_card_list[0]
    monster2 = devide_card_list[1]
    monster3 = []
    monster4 = []
    monster5 = []

    # 더미 카드 랜덤으로 뽑을 놈
    monster_list = [monster2, monster3, monster4, monster5]

    if player == 4:
        monster3 = devide_card_list[2]
        monster4 = devide_card_list[3]
    elif player > 4:
        monster3 = devide_card_list[2]
        monster4 = devide_card_list[3]
        monster5 = devide_card_list[4]

    # 게임시작
    time.sleep(0.5)
    print('마술사의 방에 오신걸 환영합니다.')
    time.sleep(1)
    print(f'플레이어는 {player}명 입니다.')
    time.sleep(1)
    print('같은 문양이 5개가 되면 아무키나 누르세요.')
    time.sleep(1)
    print('카드가 없어지면 게임이 끝납니다.')
    time.sleep(0.5)
    print('\n')
    time.sleep(0.5)
    print('플레이를 시작합니다.')
    time.sleep(0.5)
    print('\n')
    time.sleep(0.5)

    count = 0

    # 한바퀴 돌면 필드의 인덱스에 대체

    # input 유무에 따라 다른 결과를 보여줌###얘 찾은거

    def time_input(timeout=ran_time()):
        start_time = time.time()
        str_input = ''
        while True:
            if msvcrt.kbhit():
                chr = msvcrt.getche()
                if ord(chr) == 13:  # enter_key
                    str_input += str('_')
                    return 'OK'
                elif ord(chr) >= 32:  # space_char
                    str_input += str(chr)
                    return 'OK'

            if len(str_input) == 0 and (time.time() - start_time) > timeout:
                return 'No'

    # 카드 숫자가 5가 되면 뿌려야 함

    def count_card(strawberry, banana, watermelon, green_apple):
        if strawberry == 5 or banana == 5 or watermelon == 5 or green_apple == 5:
            if time_input() == 'OK':
                my_card[len(my_card):len(my_card)] = dummy
                my_card[len(my_card):len(my_card)] = field
                dummy.clear()
                field.clear()
                print(f'종을 치는데 성공했어요. 카드를 가져옵니다.')
                print(f'당신의 카드는 {len(my_card)}장 남았습니다.\n')

            elif time_input() == 'No':
                str_monster = random.choice(monster_list)
                str_monster[len(str_monster):len(str_monster)] = dummy
                str_monster[len(str_monster):len(str_monster)] = field
                dummy.clear()
                field.clear()
                print(f'이런... 상대가 종을 쳤어요.')

        elif strawberry != 5 and banana != 5 and watermelon != 5 and green_apple != 5:
            if time_input() == 'OK':
                for idx, m in enumerate(monster_list):
                    if len(m) != 0:
                        m.append(my_card[idx])
                        my_card.pop(idx)
                print(f'틀렸어요. 벌칙으로 카드를 한장씩 돌립니다.')
                print(f'당신의 카드는 {len(my_card)}장 남았습니다.\n')

    # 카드 한장 내면 필드에 보여짐, 내 카드는 없어짐
    # 게임 진행 함수
    notice = '엔터 눌러 게임을 진행하세요'
    o_notice = '상대가 카드를 냅니다.'

    def my_turn():
        if len(field) <= player:
            input(notice)
            time.sleep(ran_time())
            field.append(my_card[0])
            my_card.pop(0)
            # 카드 5개인지 세는 함수
            print(field)
            strawberry = ''.join(field).count('🍓')
            banana = ''.join(field).count('🍌')
            watermelon = ''.join(field).count('🍉')
            green_apple = ''.join(field).count('🍏')
            print(f'당신의 카드는 {len(my_card)}장 남았습니다.\n')
            time.sleep(0.5)
            count_card(strawberry, banana, watermelon, green_apple)
            time.sleep(ran_time())
        else:
            input(notice)
            time.sleep(ran_time())
            field.append(my_card[0])
            my_card.pop(0)
            dummy.append(field[0])
            field.pop(0)
            print(field)
            strawberry = ''.join(field).count('🍓')
            banana = ''.join(field).count('🍌')
            watermelon = ''.join(field).count('🍉')
            green_apple = ''.join(field).count('🍏')
            print(f'당신의 카드는 {len(my_card)}장 남았습니다.\n')
            time.sleep(0.5)
            count_card(strawberry, banana, watermelon, green_apple)
            time.sleep(ran_time())

    def other(auto_player):
        if len(field) <= player:
            field.append(auto_player[0])
            auto_player.pop(0)
            print(field)
            strawberry = ''.join(field).count('🍓')
            banana = ''.join(field).count('🍌')
            watermelon = ''.join(field).count('🍉')
            green_apple = ''.join(field).count('🍏')
            time.sleep(0.5)
            count_card(strawberry, banana, watermelon, green_apple)
            time.sleep(ran_time())
        else:
            field.append(auto_player[0])
            auto_player.pop(0)
            dummy.append(field[0])
            field.pop(0)
            print(field)
            strawberry = ''.join(field).count('🍓')
            banana = ''.join(field).count('🍌')
            watermelon = ''.join(field).count('🍉')
            green_apple = ''.join(field).count('🍏')
            time.sleep(0.5)
            count_card(strawberry, banana, watermelon, green_apple)
            time.sleep(ran_time())

    while True:
        if len(my_card) == 0:
            print('당신의 패배입니다.')
            break

        elif len(monster2) == 0 and len(monster3) == 0 and len(monster4) == 0 and len(monster5) == 0:
            print('당신이 이겼어요.')
            break

        # 카드 놀이 시작
        # 필드에 n장이 쌓이면 앞에꺼부터 없어짐
        else:
            my_turn()
            other(monster2)

            if monster4 != []:
                other(monster3)
                other(monster4)

                if monster5 != []:
                    other(monster5)
                else:
                    pass
            else:
                pass
