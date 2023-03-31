import time
import os
from rich.console import Console
from rich.table import Table
from rich import print
from charactor import *
from monster import *
import random

# 인트로


def intro():
    print("-"*53)
    typing("안녕하세요, 무지성 탑에 어서오세요 !")
    time.sleep(1)


def make_monster(difficulty, stage):
    slime = Slime(stage)
    skeleton = Skeleton(stage)
    zombie = Zombie(stage)
    monsters = [slime, skeleton, zombie]
    monsters_list = []
    for i in range(1, int(difficulty)+1):
        monsters_list.append(random.choice(monsters))
    return monsters_list


def alive_check(monsters_list):
    for monster in monsters_list:
        if monster.hp == 0:
            del monsters_list[monsters_list.index(monster)]
    return monsters_list


def job_table(job_dict):
    console = Console()
    table = Table(title='직업 리스트', show_header=True)
    column_list = ['Class', 'H P', 'M P', 'Power', 'Magic', 'Avoid']
    for column in column_list:
        table.add_column(column, justify='center', width=10)
    # for row in job.Job.job_dict
    for job in job_dict:
        # table.add_row(job_dict[job])
        table.add_row(job_dict[job]["job"],
                      str(job_dict[job]["hp"]),
                      str(job_dict[job]["mp"]),
                      str(job_dict[job]["power"]),
                      str(job_dict[job]["magic_power"]),
                      str(job_dict[job]["avoid"]),
                      )
    return console.print(table)

# 타이핑치는 효과 str


def typing(text):
    for i in range(len(text)):
        print(text[i], end='', flush=True)
        time.sleep(0.03)
    print('')


def select_difficulty():
    typing('난이도에 따라 몬스터의 수가 바뀝니다')
    typing('쉬움 : 1, 보통 : 2, 어려움 : 3')
    while True:
        difficulty = input('난이도를 선택해주세요(1,2,3) : ')
        if difficulty in ['1', '2', '3']:
            break
        else:
            typing('1,2,3 중에 하나를 골라주세요')
    dic = {'1': '쉬움', '2': '보통', '3': '어려움'}
    typing(f'{dic[difficulty]} 난이도로 시작합니다')
    time.sleep(1.5)
    os.system('cls')
    return difficulty

# 타이핑치는 효과 list


def list_typing(list):
    for item in list:
        typing(item)


def ui_main(text):
    console = Console()
    table = Table(show_header=False, width=92)
    for i in text:
        table.add_row(i)
    return console.print(table)


def ui_table(stage, round, user_charactor, monsters_list):
    console = Console()
    table = Table(title=f'{stage} 층 전투 상태창',show_header=True)
    column_list = ['Turn '+str(round), 'Name', 'H P',
                   'M P', 'Power', 'Magic', 'Avoid']
    for i in column_list:
        table.add_column(i, justify='center', width=10)
    table.add_row(
        str(user_charactor.lv),
        user_charactor.name,
        str(user_charactor.hp)+" / "+str(user_charactor.max_hp),
        str(user_charactor.mp)+" / "+str(user_charactor.max_mp),
        str(user_charactor.power),
        str(user_charactor.magic_power),
        str(user_charactor.avoid),
    )
    for monsters in monsters_list:
        table.add_row(
            str(monsters.lv),
            monsters.name,
            str(monsters.hp)+" / "+str(monsters.max_hp),
            str(monsters.mp)+" / "+str(monsters.max_mp),
            str(monsters.power),
            str(monsters.magic_power),
            str(monsters.avoid),
        )
    return console.print(table)


def next_floor(stage):
    typing(f"당신은 조심해서 {stage} 층으로 향합니다")
    time.sleep(2)
    os.system('cls')
    typing("왠지 불길한 기운이 앞에 있습니다")
    time.sleep(2)
    os.system('cls')
    typing("이런 !! 몬스터를 만났습니다 !")
    typing("전투가 시작됩니다 준비해주세요 !")
    typing("3  .   .   2  .   .   1  .   .   ")
    time.sleep(1)
    os.system('cls')


def select_action(monsters_list):
    while True:
        print('공격 : 1, 마법공격 : 2, 스킬 : 3')
        action = input('무엇을 하시겠습니까? : ')
        if action in ['1', '2', '3']:
            break
        else:
            typing('1,2,3 중에 하나를 골라주세요')
    print('누굴 공격?')

    str_list = ''
    target_list = []
    for idx, value in enumerate(monsters_list):
        str_list += str(idx+1)+' : '+str(value.name)+'\n'
        target_list.append(f'{idx+1}')

    while True:
        target = input(str_list)
        if target in target_list:
            break
        else:
            typing('몬스터를 골라주세요')
    return action, monsters_list[int(target)-1]


def monster_attack(user_charactor, monsters_list):
    for monster in monsters_list:
        ui_main(monster.random_attack(user_charactor))


def attack_target(user_charactor, action, target):
    if action == '1':
        ui_main(user_charactor.attack(target))
    elif action == '2':
        ui_main(user_charactor.magic_attack(target))
    else:
        if user_charactor.job == '전사':
            ui_main(user_charactor.warrior_skil_1(target))
        elif user_charactor.job == '마법사':
            ui_main(user_charactor.wizard_skil_1())
        elif user_charactor.job == '도적':
            ui_main(user_charactor.thief_skil_1())
        else:
            ui_main(user_charactor.archer_skil_1(target))


def endturn_mp_get(user_charactor, monsters_list):
    user_charactor.mp_get()
    for monster in monsters_list:
        monster.mp_get()


def inform_game():
    text = '''
            무지성월드에 오신것을 환영합니다. 
            1층 부터 10층 까지 층별로 진화하는 몬스터를 물리치고 성을 정복해보세요. 
            중간 중간 스페셜 게임도 준비되어있습니다. 
            '''
    typing(text)


def inter_tower():
    text = '당신은 끝이 보이지 않는 탑의 입구로 들어갑니다.'
    typing(text)
