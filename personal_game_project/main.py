import random
import time
# 사운드
import winsound


class Character:
    """
    모든 캐릭터의 모체가 되는 클래스
    """

    def __init__(self, name, hp=100, power=10, mana=0, magic_power=0):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power
        self.max_mana = mana
        self.mana = 0
        self.magic_power = magic_power

    def attack(self, other):
        damage = random.randint(self.power - 2, self.power + 2)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 일반 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.\n"
              f'{other.name}의 현재 HP:{other.hp}')
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def power_attack(self, other):
        damage = random.randint(self.power, self.power + 5)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 강한 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.\n"
              f'{other.name}의 현재 HP:{other.hp}')
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def monster_attack(self):
        monster.attack_type = random.randint(1, 2)
        if monster.attack_type == 1:
            monster.attack(player)
        elif monster.attack_type == 2:
            monster.power_attack(player)

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

    def __init__(self, name='seman', hp=250, power=15, mana=15, magic_power=20):
        self.hp = hp
        self.max_hp = hp
        self.power = power
        # self.name = name
        self.name = input('플레이어명을 입력해주세요 :')
        self.magic_power = magic_power
        self.max_mana = mana
        self.mana = mana//2

    def player_attack_select(self):
        while True:
            player.show_status()
            print()
            monster.show_status()

            print('\n'
                  f'{player.name}의 턴\n'
                  f'일반 공격:1 마법 공격:2 회복 마법:3 명상:4')
            player.attack_type = input('행동 선택: ')
            print()
            if player.attack_type == '1':
                player.attack(monster)
                break
            # 마나 있는 상태로 마법 공격 시도 먼저 if문 돌고 없으면 다음
            elif player.attack_type == '2' and self.mana >= 5:
                player.magic_attack(monster)
                break
            # 마나 없는 상태로 마법 공격 시도
            elif player.attack_type == '2':
                player.magic_attack(monster)
                continue
            elif player.attack_type == '3' and self.mana >= 10:
                player.heal()
                break
            elif player.attack_type == '3':
                player.heal()
                continue
            elif player.attack_type == '4':
                player.meditation()
                break
            else:
                print(f'{player.attack_type}은 올바른 입력값이 아닙니다.'
                      '\n')
                continue

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

    def heal(self):
        mana_consum = 10
        if self.mana < mana_consum:
            print(f'마나가 {mana_consum-self.mana}만큼 모자랍니다')
        else:
            self.mana -= mana_consum
            heal = random.randint(self.magic_power, self.magic_power * 2)
            self.hp += heal
            if self.max_hp < self.hp:
                self.hp = self.max_hp
            print(
                f'마나 {mana_consum}을 소모합니다.\n'
                f'{self.name}의 회복 마법! {self.name}이(가) {heal}만큼 회복하였습니다.\n'
                f'{self.name}의 현재 HP:{self.hp}')

    def meditation(self):
        mana_recovery = random.randint(1, self.magic_power/2)
        self.mana += mana_recovery
        if self.max_mana < self.mana:
            self.mana = self.max_mana

        print(
            f'{self.name}의 명상! {self.name}이(가) {mana_recovery}만큼 회복하였습니다.\n'
            f'{self.name}의 현재 MP:{self.mana}')


class Slime(Character):

    def __init__(self):
        self.hp = 100
        self.max_hp = 100
        self.power = 5
        self.max_mana = 0
        self.mana = 0
        self.magic_power = 0
        self.name = 'Slime'


class Skeleton(Character):

    def __init__(self):
        self.hp = 120
        self.max_hp = 120
        self.power = 15
        self.max_mana = 5
        self.mana = 0
        self.magic_power = 20
        self.name = 'Skeleton'

    def bone_magic(self, other):
        self.mana -= self.max_mana
        damage = random.randint(self.power+3, self.magic_power+self.power)
        other.hp = max(other.hp - damage, 0)
        print(
            f'마나 {self.max_mana}을 소모합니다.\n'
            f"{self.name}의 뼈 마법!  {other.name}에게 {damage}의 데미지를 입혔습니다.\n"
            f'{other.name}의 현재 HP:{other.hp}')
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def skeleton_attack(self):
        # 마나 체크 후 공격 타입 지정
        if self.mana == self.max_mana:
            monster.attack_type = 3
        else:
            monster.attack_type = random.randint(1, 2)
        if monster.attack_type == 1:
            monster.attack(player)
        elif monster.attack_type == 2:
            monster.power_attack(player)
        elif monster.attack_type == 3:
            monster.bone_magic(player)


class Zombie(Character):

    def __init__(self):
        self.max_hp = 200
        self.hp = random.randrange(self.max_hp+1)
        self.power = random.randint(10, 15)
        self.max_mana = 4
        self.mana = 0
        self.magic_power = 0
        self.name = 'Zombie'

    def recovery(self):
        self.mana -= self.max_mana
        # 턴 수 * 2로 회복 전역 변수 global 사용
        recovery = turn*2
        self.hp += recovery
        if self.max_hp < self.hp:
            self.hp = self.max_hp
        print(
            f'마나 {self.max_mana}을 소모합니다.\n'
            f'{self.name}의 회복! {self.name}이(가) {recovery}만큼 회복하였습니다.\n'
            f'{self.name}의 현재 HP:{self.hp}')

    def zombie_attack(self):
        # 마나 체크 후 공격 타입 지정
        if self.mana == self.max_mana:
            monster.attack_type = 3
        else:
            monster.attack_type = random.randint(1, 2)
        if monster.attack_type == 1:
            monster.attack(player)
        elif monster.attack_type == 2:
            monster.power_attack(player)
        elif monster.attack_type == 3:
            monster.recovery()


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
# 랜덤 몬스터 생성
monster = random.choice(monster_list)
# 플레이어 패배 체크용 몬스터
# monster = Defeat()
player = Player()


class Battle():
    print()
    loading(4)

    def stage():
        global turn
        turn = 0
        while True:
            turn += 1
            player.mana += 1
            monster.mana += 1

            # 플레이어 턴
            print(f'{turn}턴 ', end='')
            player.player_attack_select()
            print()

            # 몬스터 처치
            if monster.hp == 0:
                score = (player.hp+player.mana*5 +
                         monster.max_hp//3)*(20-turn)
                if score <= 0:
                    score = 0
                winsound.PlaySound('./sound/good.wav',
                                   winsound.SND_FILENAME)
                print(f'{player.name}의 승리입니다!\n'
                      f'score = {score}')
                break

            # 몬스터 턴
            # 이름 체크 후 다른 행동 패턴 실행
            if monster.name == 'Zombie':
                monster.zombie_attack()
            elif monster.name == 'Skeleton':
                monster.skeleton_attack()
            else:
                monster.monster_attack()
            print()
            # 플레이어 패배
            if player.hp == 0:
                score = (monster.max_hp-monster.hp)//5
                print(f'{player.name}의 패배입니다.\n'
                      f'score = {score}')
                if score <= 0:
                    score = 0
                winsound.PlaySound('./sound/bad.wav',
                                   winsound.SND_FILENAME)
                break


Battle.stage()
