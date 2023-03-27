import random
import time
# 사운드
import winsound


class Character:
    """
    모든 캐릭터의 모체가 되는 클래스
    """

    def __init__(self, name, hp, power):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power
        self.max_mana = 0
        self.mana = 0
        self.magic_power = 0

    def attack(self, other):
        damage = random.randint(self.power - 2, self.power + 2)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 일반 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.\n"
              f'{other.name}의 현재 HP:{other.hp}')
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def power_attack(self, other):
        damage = random.randint(self.power, self.power * 2)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 강한 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.\n"
              f'{other.name}의 현재 HP:{other.hp}')
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def magic_attack(self, other):
        mana_consum = 5
        if self.mana < mana_consum:
            print(f'마나가 {mana_consum-self.mana}만큼 모자랍니다')
        else:
            self.mana -= mana_consum
            damage = random.randint(self.magic_power, self.magic_power + 5)
            other.hp = max(other.hp - damage, 0)
            print(
                f'마나 {mana_consum}을 소모합니다.\n'
                f"{self.name}의 마법 공격!  {other.name}에게 {damage}의 데미지를 입혔습니다.\n"
                f'{other.name}의 현재 HP:{other.hp}')
            if other.hp == 0:
                print(f"{other.name}이(가) 쓰러졌습니다.")

    def player_attack(self):
        while True:
            print(f'{player.name}의 차례\n'
                  f'일반 공격:1 마법 공격:2')
            player.attack_type = input()
            if player.attack_type == '1':
                player.attack(monster)
                break
            elif player.attack_type == '2':
                player.magic_attack(monster)
                break
            else:
                print('choice 1 or 2')
                continue

    def monster_attack(self):
        player.attack_type = random.randint(1, 2)
        if player.attack_type == 1:
            monster.attack(player)
        elif player.attack_type == 2:
            monster.power_attack(player)
        else:
            print('error')

    def show_status(self):
        # 최대 체력 제한
        if self.max_hp < self.hp:
            self.hp = self.max_hp
        # 최대 마나량 제한
        if self.max_mana < self.mana:
            self.mana = self.max_mana
        print(f"{self.name}의 상태 \nHP:{self.hp}/{self.max_hp} STR:{self.power}\n"
              f"MP:{self.mana}/{self.max_mana}   INT:{self.magic_power}")


class Player(Character):

    def __init__(self):
        self.hp = 300
        self.max_hp = 300
        self.power = 10
        # self.name = input('플레이어명을 입력해주세요 : ')
        self.name = 'seman'
        self.magic_power = 20
        self.max_mana = 15
        self.mana = 15


class Slime(Character):

    def __init__(self):
        self.hp = 100
        self.max_hp = 100
        self.power = 3
        self.max_mana = 0
        self.mana = 0
        self.magic_power = 0
        self.name = 'Slime'


class Skeleton(Character):

    def __init__(self):
        self.hp = 80
        self.max_hp = 80
        self.power = 15
        self.max_mana = 0
        self.mana = 0
        self.magic_power = 0
        self.name = 'Skeleton'


class Zombie(Character):

    def __init__(self):
        self.max_hp = random.randint(100, 350)
        self.hp = random.randrange(self.max_hp+1)
        self.power = random.randint(5, 20)
        self.max_mana = 0
        self.mana = 0
        self.magic_power = 0
        self.name = 'Zombie'


class Defeat(Character):

    def __init__(self):
        self.hp = 999
        self.max_hp = 999
        self.power = 999
        self.max_mana = 0
        self.mana = 0
        self.magic_power = 0
        self.name = 'Defeat'


def loading(num):
    # 시작시 로딩 출력
    for i in range(1, num):
        print('loading... ', num-i, 'second', sep='')
        time.sleep(1)
        print()
    print('Game Start')
    print()


monster_list = [Slime(), Skeleton(), Zombie()]
# 랜덤 몬스터
monster = random.choice(monster_list)
# 플레이어 패배 체크용
# monster = Defeat()
player = Player()


class Battle():
    # loading(4)

    def stage():
        turn = 0
        while True:
            turn += 1
            # 2턴마다 마나 1 회복
            if turn % 2 == 0:
                player.mana += 1
                monster.mana += 1

            # 매턴 status 출력
            player.show_status()
            print()
            monster.show_status()
            print()
            # time.sleep(1)
            # 플레이어 턴
            print(f'{turn}턴 ', end='')
            player.player_attack()
            print()
            # time.sleep(1)

            # 몬스터 턴
            monster.monster_attack()
            print()
            # time.sleep(1)
            # 플레이어 패배
            if player.hp == 0:
                score = (monster.max_hp-monster.hp)//5
                print(f'{player.name}의 패배입니다.\n'
                      f'score = {score}')
                winsound.PlaySound('./sound/bad.wav',
                                   winsound.SND_FILENAME)
                break

            # 몬스터 처치
            if monster.hp == 0:
                score = (player.hp+player.mana*5 +
                         monster.max_hp//3)*(20-turn)
                winsound.PlaySound('./sound/good.wav',
                                   winsound.SND_FILENAME)
                print(f'{player.name}의 승리입니다!\n'
                      f'score = {score}')
                break
                # 중간 스코어
                # sum_score += score
                # 스테이지 기능
                # while True:
                #     print('계속 도전하시겠습니까? Y/N')
                #     stage_continue = input()
                #     if stage_continue == 'Y':
                #         # new_monster = random.choice(monster_list)
                #         # monster = new_monster
                #         # break
                #         #     elif stage_continue == 'N':
                #         #         break
                #         #     else:
                #         #         print('YorN')
                #         #     continue
                #         # break


Battle.stage()
