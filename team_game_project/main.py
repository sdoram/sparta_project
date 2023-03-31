from charactor import *
from event import *
from monster import *
from script import *
import time

# 전역변수 정의
stage = 1
turn = 3
user = User()

item = Item()
inventory = Inventory()

# while 시작(stage)
while stage<=10:
    # 게임 인트로
    ###################################################
    # stage = 1이면 실행
    if stage == 1:
        intro()

        # 난이도 선택 > 쉬움 몹1, 보통 몹2, 어려움 몹3
        difficulty = select_difficulty()

        # # 게임 소개
        inform_game()

        # # 유저 정보 받기
        typing(user.input_id())
        time.sleep(1.5)
        # 직업 선택
        os.system('cls')
        job_table(user.job_dict)
        user_charactor = user.job_select()
        # 탑으로 입장
        inter_tower()
        time.sleep(1.5)
        os.system('cls')

    ###################################################
    
    

    # 몬스터 생성
    monsters_list = make_monster(difficulty,stage)

    # 전투 시작(round)
    while True:
        os.system('cls')
        # 몬스터 조우
        # 유저테이블 몬스터 테이블 따로
        ui_table(stage,turn, user_charactor, monsters_list)

        # 행동 및 타겟 선택
        while True:
            action, target = select_action(monsters_list)
            if action == '2' or action == '3': 
                if user_charactor.mp >= 5:
                    attack_target(user_charactor, action, target)
                    turn+=1
                    break
                else: print('마나가 부족합니다 다른 공격을 선택해주세요')
            else: 
                attack_target(user_charactor, action, target)
                turn+=1
                break
        
        # 공격하기전에 몬스터 생존여부 확인 후 공격
        monsters_list = alive_check(monsters_list)
        if monsters_list != []: 
            monster_attack(user_charactor, monsters_list)
            endturn_mp_get(user_charactor, monsters_list)
        else: 
            endturn_mp_get(user_charactor, monsters_list)
            break
        if user_charactor.hp == 0: 
            typing('당신은 치명상을 입었습니다')
            break
        time.sleep(2)
        os.system('cls')
    # 전투 종료
    ###################################################

    # 전투 종료 메세지
    if user_charactor.hp == 0: 
        typing('You Died')
        break
    else : 
        typing('전투에 승리했습니다 !')
        time.sleep(1)

    # 아이템 드랍
    # drop_random = random.randint(1, 100)
    # 드랍률 고정
    drop_random = 0
    if drop_random < 10:
        drop_item(user_charactor)

    # 스테이지 클리어 이벤트
    stage_clear(stage,user_charactor)

    # 다음 층으로
    stage+=1
    user_charactor.lv+=1
    next_floor(stage)
    ###################################################

typing('Game Clear')