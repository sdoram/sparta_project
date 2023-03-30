import random
# 직업
# 직업 스킬


class BaseCharactor:
    def __init__(self, name, lv, hp, mp, power, magic_power, avoid):
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
            damage = random.randint(int(self.power*0.8), int(self.power*1.2))
            other.hp = max(other.hp - damage, 0)
            text = [f'{self.name}이 {other.name}을 {damage}의 데미지로 공격']
            if other.hp == 0:
                text.append(f'{other.name}이(가) 쓰러졌습니다.')
        else:
            text = [f'{self.name}의 공격이 실패']
        return text

    def power_attack(self, other):
        mp_consum = 5
        miss = other.avoid/100
        result = random.choices(range(0, 2), weights=[miss, 1-miss])
        if self.mp > mp_consum:
            if result == [1]:
                damage = random.randint(
                    int(self.power*0.8), int(self.power*1.2))
                other.hp = max(other.hp - damage, 0)
                text = [f'{self.name}이 {other.name}을 {damage}의 데미지로 필살 공격 !!!']
                if other.hp == 0:
                    text.append(f'{other.name}이(가) 쓰러졌습니다.')
            else:
                text = [f'{self.name}의 필살 공격이 실패']
        else:
            text = [f'마나가 {mp_consum-self.mp} 만큼 부족합니다']
        return text

    def magic_attack(self, other):
        damage = random.randint(self.magic_power*0.8, self.magic_power*1.2)
        other.hp = max(other.hp - damage, 0)
        text = [f'{self.name}이 {other.name}을 {damage}의 데미지로 마법공격']
        if other.hp == 0:
            text = [f'{self.name}의 공격이 실패']
        return text

    def show_status(self):
        print(self.name, self.lv, self.hp, self.mp,
              self.power, self.magic_power, self.avoid)

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


class User(BaseCharactor):
    def __init__(self, name=None, lv=None, hp=100, mp=100, power=10, magic_power=10, avoid=10, job=None, gold=None):
        super().__init__(name, lv, hp, mp, power, magic_power, avoid)
        self.job = job
        self.gold = gold
        self.job_dict = {
            '1': {
                'job': '전사',
                'hp': random.randint(int(self.hp*1.8), int(self.hp*2.5)),
                'mp': self.mp,
                'power': random.randint(int(self.power*1.8), int(self.power*3)),
                'magic_power': self.magic_power,
                'avoid': self.avoid
            },
            '2': {
                'job': '마법사',
                'hp': self.hp,
                'mp': random.randint(int(self.mp*1.8), int(self.mp*2.5)),
                'power': self.power,
                'magic_power': random.randint(int(self.magic_power*1.8), int(self.magic_power*3)),
                'avoid': self.avoid
            },
            '3': {
                'job': '궁수',
                'hp': random.randint(self.hp, int(self.hp*1.5)),
                'mp': random.randint(self.mp, int(self.mp*1.5)),
                'power': random.randint(self.power, int(self.power*2)),
                'magic_power': random.randint(int(self.magic_power*1.5), int(self.magic_power*2)),
                'avoid': random.randint(int(self.avoid*1.5), int(self.avoid*2))
            },
            '4': {
                'job': '도적',
                'hp': random.randint(self.hp, int(self.hp*1.5)),
                'mp': random.randint(self.mp, int(self.mp*1.5)),
                'power': random.randint(int(self.power*1.5), int(self.power*2)),
                'magic_power': random.randint(self.magic_power, int(magic_power*1.5)),
                'avoid': random.randint(int(self.avoid*2), int(self.avoid*3))
            },
        }

    def input_id(self):
        self.name = input('당신의 이름을 알려주세요 : ')
        print(f'당신의 이름은 {self.name} 입니다')

    def job_select(self):
        while True:
            print('전사:1 마법사:2 궁수:3 도적:4')
            self.job = input('직업을 선택해주세요 : ')
            if self.job in self.job_dict.keys():
                user = User(
                    self.name,
                    1,
                    self.job_dict[self.job]['hp'],
                    self.job_dict[self.job]['mp'],
                    self.job_dict[self.job]['power'],
                    self.job_dict[self.job]['magic_power'],
                    self.job_dict[self.job]['avoid'],
                    self.job_dict[self.job]['job'],
                )
                break
            else:
                print('올바른 값을 입력해주세요')
                continue
        print(f'당신의 직업은 {self.job_dict[self.job]["job"]} 입니다')
        return user

    def show_status(self):
        print(f'name = {self.name}\nlv = {self.lv}\nhp = {self.hp}\nmp = {self.mp}\npower = {self.power}\nmagic_power = {self.magic_power}\navoid = {self.avoid}\njob = {self.job}')


class Warrior:
    def warrior_skil_1(self, other):
        mp_consum = 5
        if self.mp < mp_consum:
            text = [f'마나가{mp_consum - self.mp}만큼 모자랍니다']
        else:
            self.mp -= mp_consum
            damage = random.randint(self.power, self.power*1.2)
            other.hp = max(other.hp - damage, 0)
            text = [
                f'마나 {mp_consum}을 소모합니다.\n'
                f"{self.name}의 마법 공격!  {other.name}에게 {damage}의 데미지를 입혔습니다.\n"
                f'{other.name}의 현재 HP:{other.hp}']
            if other.hp == 0:
                text.append = [f"{other.name}이(가) 쓰러졌습니다."]
        return text


class Wizard:
    def wizard_skil_1(self, other):
        mp_consum = 5
        if self.m < mp_consum:
            text = [f'마나가{mp_consum - self.mp}만큼 모자랍니다']
        else:
            self.mp -= mp_consum
            damage = random.randint(self.magic_power, self.magic_power*2)
            other.hp = max(other.hp - damage, 0)
            text = [
                f'마나 {mp_consum}을 소모합니다.\n'
                f"{self.name}의 마법 공격!  {other.name}에게 {damage}의 데미지를 입혔습니다.\n"
                f'{other.name}의 현재 HP:{other.hp}']
            if other.hp == 0:
                text.append = [f"{other.name}이(가) 쓰러졌습니다."]
        return text


class Thief:
    def thief_skil_1(self, other):
        mp_consum = 5
        if self.mp < mp_consum:
            text = [f'마나가{mp_consum - self.mp}만큼 모자랍니다']
        else:
            self.mp -= mp_consum
            damage = random.randint(self.magic_power, self.magic_power + 5)
            other.hp = max(other.hp - damage, 0)
            text = [
                f'마나 {mp_consum}을 소모합니다.\n'
                f"{self.name}의 마법 공격!  {other.name}에게 {damage}의 데미지를 입혔습니다.\n"
                f'{other.name}의 현재 HP:{other.hp}']
            if other.hp == 0:
                text.append = [f"{other.name}이(가) 쓰러졌습니다."]
        return text


class Archer:
    def archer_skil_1(self, other):
        mp_consum = 5
        if self.mp < mp_consum:
            text = [f'마나가{mp_consum - self.mp}만큼 모자랍니다']
        else:
            self.mp -= mp_consum
            damage = random.randint(self.magic_power, self.magic_power + 5)
            other.hp = max(other.hp - damage, 0)
            text = [
                f'마나 {mp_consum}을 소모합니다.\n'
                f"{self.name}의 마법 공격!  {other.name}에게 {damage}의 데미지를 입혔습니다.\n"
                f'{other.name}의 현재 HP:{other.hp}']
            if other.hp == 0:
                text.append = [f"{other.name}이(가) 쓰러졌습니다."]
        return text


class Item(BaseCharactor):
    def __init__(self, name=None, lv=None, hp=None, mp=None, power=None, magic_power=None, avoid=None):
        super().__init__(name, lv, hp, mp, power, magic_power, avoid)


sub_random = random.randint(1, 3)
main_random = random.randint(3, 5)


item_list = {
    1: Item(name='wand', mp=sub_random, magic_power=main_random),
    2: Item(name='greatsword', hp=sub_random, power=main_random),
    3: Item(name='knife', power=sub_random, avoid=main_random),
    4: Item(name='bow', hp=main_random, avoid=sub_random),


}


class Inventory(BaseCharactor):
    def __init__(self, name=None, lv=None, hp=None, mp=None, power=None, magic_power=None, avoid=None):
        super().__init__(name, lv, hp, mp, power, magic_power, avoid)


shopping_list = {
    1: Inventory(name='hp potion', hp=10),
    2: Inventory(name='mp potion', mp=5),
    3: Inventory(name='용의 비늘(power +5)', power=10),
    4: Inventory(name='magic_power up', magic_power=10),
}
