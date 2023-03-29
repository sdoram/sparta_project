import random
import time
import os
from rich.console import Console
from rich.table import Table
from rich import print
from job import *
# from event import *
# from monster import *

# 인트로


def intro():
    print("-"*53)
    typing("안녕하세요, 무지성 탑에 어서오세요 !")
    time.sleep(1)


def job_table():
    console = Console()
    table = Table(show_header=True)
    column_list = ['Class', 'H P', 'M P', 'Power', 'Magic', 'Avoid']
    for column in column_list:
        table.add_column(column, justify='center', width=10)
    # for row in job.Job.job_dict
    table.add_row("도적", "150", "20", "10", "20", "20")
    return console.print(table)

# 타이핑치는 효과 str


def typing(text):
    for i in range(len(text)):
        print(text[i], end='', flush=True)
        time.sleep(0.03)
    print('')

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


def ui(*args):
    console = Console()
    table = Table(show_header=True)
    column_list = ['Round '+str(round), 'Name', 'H P',
                   'M P', 'Power', 'Magic', 'Avoid']
    for i in column_list:
        table.add_column(i, justify='center', width=10)
    for arg in args:
        table.add_row(
            str(arg.lv),
            arg.name,
            str(arg.hp)+" / "+str(arg.max_hp),
            str(arg.mp)+" / "+str(arg.max_mp),
            str(arg.power),
            str(arg.magic_power),
            str(arg.avoid),
        )
    return console.print(table)


def next_floor():
    typing("당신은 조심해서 층을 올라갑니다")
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


class Info:
    def __init(self, name=None, job_select=None):
        self.name = name
        self.job_select = job_select

    def input_id(self):
        self.name = input('당신의 이름을 알려주세요 : ')
        return self.name


class BaseCharactor:
    def __init__(self, name=str, lv=int, hp=int, mp=int, power=int, magic_power=int, avoid=int):
        # 캐릭터들 기본 스텟
        self.name = name
        self.lv = lv
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.power = power
        self.magic_power = magic_power
        self.avoid = avoid

    def attack(self, other):
        miss = other.avoid/100
        result = random.choices(range(0, 2), weights=[miss, 1-miss])
        if result == [1]:
            damage = random.randint(self.power*0.8, self.power*1.2)
            other.hp = max(other.hp - damage, 0)
            text = [f'{self.name}이 {other.name}을 {damage}의 데미지로 공격']
            if other.hp == 0:
                text.append(f'{other.name}이(가) 쓰러졌습니다.')
        else:
            text = [f'{self.name}의 공격이 실패']
        return text

    def magic_attack(self, other):
        damage = random.randint(self.magic_power*0.8, self.magic_power*1.2)
        other.hp = max(other.hp - damage, 0)
        text = [f'{self.name}이 {other.name}을 {damage}의 데미지로 마법공격']
        if other.hp == 0:
            text = [f'{self.name}의 공격이 실패']
        return text

    def show_status(self):
        print('플레이어명', self.name, 'LV', self.lv, 'HP', self.hp, 'MP', self.mp,
              'power', self.power, 'magic_power', self.magic_power, 'avoid', self.avoid, '직업', self.job, 'gold', self.gold)
        return ''

    # 공격함수
    # 공격할때 other를 받아서 피해를 줘야함
    # 일정확률도 회피?

    # 스테이터스 보여줘야함


class User(BaseCharactor):
    def __init__(self, name, lv, hp, mp, power, magic_power, avoid, job, gold=None):
        super().__init__(name, lv, hp, mp, power, magic_power, avoid)
        self.job = job
        self.gold = gold
    # 전투 중 몬스터 몇 마리 만날 것인지?
    # 경험치 : 경험치 테이블도 만들어야 함 > 경험치를 넣어주면 레벨을 리턴
    # 레벨업 시 모든 체력과 마나 회복
    # 몬스터 보상 : 골드, 경험치

    # 전투중 랜덤으로 서브 몬스터 추가됨
    # 캐릭터 선택 후 난이도 선택에 따른 몬스터 공격력, HP량, 스킬횟수 증가 ex) 하수, 중수, 고수

    # 직업 전용스킬
    # 회복

    # 플레이어 공격방식 선택
    # 몬스터가 랜덤 공격
    # 회복시 최대치 제한
    # 진행 턴을 계수로 받는 스킬


round = 1


# me = User(name,1,100,10,15,10,10)
# mob = monster.Monster('mob',1,20,3,4,5,50)
# mob2 = monster.Monster('mob2',1,20,3,4,5,50)
# ui(me,mob,mob2)

# ui_main(me.attack(mob))
# ui(me,mob,mob2)


if __name__ == "__main__":
    inf = Info()

    # intro()
    name = inf.input_id()
    job_table()
    # next_floor()

    job_status = Job.job_select()
    # print(job_status)
    # print(dir(job_status))
    player = User(name=name,
                  lv=1,
                  hp=job_status['hp'],
                  mp=job_status['mp'],
                  power=job_status['power'],
                  magic_power=job_status['magic_power'],
                  avoid=job_status['avoid'],
                  job=job_status['job'],
                  gold=job_status['gold']
                  )

    print(player.show_status())
