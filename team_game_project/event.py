from charactor import *
from sphinx import call_sphinx
from magician import call_magician
from script import *
import random
import time


# 아이템 드롭
def drop_item(user):
    choose_item = random.randint(1, 4)
    event_item = item_list[choose_item]
    typing(f'{event_item.name}을 획득했습니다')
    time.sleep(1)
    if choose_item == 1:
        user.max_mp += event_item.mp
        user.mp += event_item.mp
        user.magic_power += event_item.magic_power
        print(
            f'mp의 최대치가 {event_item.mp}만큼 증가하고, 현재 mp가 {event_item.mp} 만큼 회복했습니다.')
        typing(f'magic power가 {event_item.magic_power}만큼 증가했습니다.')
    elif choose_item == 2:
        user.max_hp += event_item.hp
        user.hp += event_item.hp
        user.power += event_item.power
        print(
            f'hp의 최대치가 {event_item.hp}만큼 증가하고, 현재 hp가 {event_item.hp} 만큼 회복했습니다.')
        typing(f'power가 {event_item.power}만큼 증가했습니다.')
    elif choose_item == 3:
        user.power += event_item.power
        user.avoid += event_item.avoid
        print(f'avoid가 {event_item.avoid}만큼 증가했습니다.')
        typing(f'power가 {event_item.power}만큼 증가했습니다.')
    else:
        user.max_hp += event_item.hp
        user.hp += event_item.hp
        user.avoid += event_item.avoid
        print(
            f'hp의 최대치가 {event_item.hp}만큼 증가하고, 현재 hp가 {event_item.hp} 만큼 회복했습니다.')
        typing(f'avoid가 {event_item.avoid}만큼 증가했습니다.')
    return


# 상점
def call_shop(stage, user):
    while True:
        time.sleep(1)
        typing(f'현재 보유 골드 : {user.gold} G')
        time.sleep(1)
        print(f'1 : hp_potion(hp +10) - {shopping_list[1].gold}G\n'
              f'2 : mp_potion(mp +5) - {shopping_list[2].gold}G')
        print(
            f'3 : 용의_비늘(power +10) - {shopping_list[3].gold}G\n'
            f'4 : magic_power_up(magic power +10) - {shopping_list[4].gold}G')
        typing(f'5 : 상점 나가기')
        time.sleep(0.5)
        buy = input('구매하실 아이템을 선택해주세요 : ')
        if buy in ['1', '2', '3', '4', '5']:
            # 골드 확인
            if buy == '5': break
            item_shop = shopping_list[int(buy)]
            if buy == '1':
                if user.gold >= item_shop.gold:
                    user.max_hp += item_shop.hp
                    user.hp += item_shop.hp
                    user.gold -= item_shop.gold
                    typing(f'{item_shop.name}을 구매하셨습니다.')
                    typing(f'현재 hp가 {item_shop.hp} 만큼 회복했습니다.')
                else : 
                    typing('Gold가 부족합니다')
                    continue
            elif buy == '2':
                if user.gold >= item_shop.gold:
                    user.max_mp += item_shop.mp
                    user.gold -= item_shop.gold
                    typing(f'{item_shop.name}을 구매하셨습니다.')
                    typing(f'현재 mp가 {item_shop.mp} 만큼 회복했습니다.')
                else : 
                    typing('Gold가 부족합니다')
                    continue
            elif buy == '3':
                if user.gold >= item_shop.gold:
                    user.power += item_shop.power
                    user.gold -= item_shop.gold
                    typing(f'{item_shop.name}을 구매하셨습니다.')
                    typing(f'power가 {item_shop.power}만큼 증가했습니다.')
                else : 
                    typing('Gold가 부족합니다')
                    continue
            elif buy == '4':
                if user.gold >= item_shop.gold:
                    user.magic_power += item_shop.magic_power
                    user.gold -= item_shop.gold
                    typing(f'{item_shop.name}을 구매하셨습니다.')
                    typing(f'magic power가 {item_shop.magic_power}만큼 증가했습니다.')
                else : 
                    typing('Gold가 부족합니다')
                    continue
            time.sleep(1)
            os.system('cls')
        else:
            typing('1,2,3,4,5 중 하나를 입력해주세요')
            time.sleep(1)
            os.system('cls')


# 스테이지 클리어 후
def stage_clear(stage, user):

    call_shop(stage, user)

    if stage == 5:
        call_sphinx()
        # typing(f'스핑크스 호출')

    elif stage == 10:
        call_magician()
        # typing(f'매지션 호출')

    else:
        # 일정 확률로 만나는 스테이지
        gacha = random.randint(1, 100)
        status_gocha = random.randint(5, 10)

        minus_status = random.choice(
            [user.hp, user.mp, user.power, user.magic_power])

        # 일단 체력만 감소하는걸로
        if gacha <= 10:
            typing(f'함정에 걸렸다! 체력이 {status_gocha} 만큼 감소합니다')
            minus_status -= status_gocha

        elif gacha <= 35:
            typing(f'치유의 샘 발견 !! 체력과 마나가 최대치의 {status_gocha}%만큼 회복됩니다')
            user.hp += user.max_hp*status_gocha
            if user.hp > user.max_hp:
                user.hp = user.max_hp
            user.mp += user.max_mp*status_gocha
            if user.mp > user.max_mp:
                user.mp = user.max_mp

    # 돌아가는 함수
    # next_floor()
