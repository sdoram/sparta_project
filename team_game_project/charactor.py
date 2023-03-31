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
        miss = int(other.avoid)/100
        result = random.choices(range(0, 2), weights=[miss, 1-miss])
        if result == [1]:
            damage = random.randint(int(self.power*0.8), int(self.power*1.2))
            other.hp = max(other.hp - damage, 0)
            text = [f'{self.name}이 {other.name}을 {damage}의 데미지로 공격']
            if other.hp == 0:
                text.append(f'{other.name}이(가) 쓰러졌습니다.')
                self.gold += other.gold
                text.append(f'{self.name}은(는) {other.gold}골드를 얻었습니다.')
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
                text = [
                f'{self.name}이 마나 {mp_consum}을 소모합니다.\n'
                f'{self.name}이 {other.name}을 {damage}의 데미지로 필살 공격 !!!']
                if other.hp == 0:
                    text.append(f'{other.name}이(가) 쓰러졌습니다.')
                    self.gold += other.gold
                    text.append(f'{self.name}은(는) {other.gold}골드를 얻었습니다.')
            else:
                text = [f'{self.name}의 필살 공격이 실패']
        else:
            text = [f'마나가 {mp_consum-self.mp} 만큼 부족합니다']
        return text

    def magic_attack(self, other):
        mp_consum = 5
        if self.mp < mp_consum:
            text = [f'마나가{mp_consum - self.mp}만큼 모자랍니다']
        else:
            self.mp -= mp_consum
            damage = random.randint(int(self.magic_power*0.8), int(self.magic_power*1.2))
            other.hp = max(other.hp - damage, 0)
            text = [
                f'{self.name}이 마나 {mp_consum}을 소모합니다.\n'
                f'{self.name}이 {other.name}을 {damage}의 데미지로 마법공격']
        if other.hp == 0:
            text.append(f'{other.name}이(가) 쓰러졌습니다.')
            self.gold += other.gold
            text.append(f'{self.name}은(는) {other.gold}골드를 얻었습니다.')
        return text
        
    def mp_get(self):
        self.mp += 1
        if self.mp > self.max_mp: self.mp = self.max_mp



class User(BaseCharactor):
    def __init__(self, name=None, lv=None, hp=100, mp=100, power=100, magic_power=10, avoid=10, job=None, gold=0):
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
                'mp': self.mp,
                'power': random.randint(self.power, int(self.power*2)),
                'magic_power': random.randint(int(self.magic_power*1.5), int(self.magic_power*2)),
                'avoid': random.randint(int(self.avoid*1.5), int(self.avoid*2))
            },
            '4': {
                'job': '도적',
                'hp': random.randint(self.hp, int(self.hp*1.5)),
                'mp': self.mp,
                'power': random.randint(int(self.power*1.5), int(self.power*2)),
                'magic_power': random.randint(self.magic_power, int(magic_power*1.5)),
                'avoid': random.randint(int(self.avoid*2), int(self.avoid*3))
            },
        }

    def input_id(self):
        while True:
            self.name = input('당신의 이름을 알려주세요 : ')
            if self.name =='':
                print('다시 입력해주세요')
                continue
            else: break
        text = f'당신의 이름은 {self.name} 입니다'
        return text

    def job_select(self):
        while True:
            print('1 : 전사, 2 : 마법사, 3 : 궁수, 4 : 도적')
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

    def warrior_skil_1(self, other):
        # 흡혈 스킬
        mp_consum = 5
        if self.mp < mp_consum:
            text = [f'마나가{mp_consum - self.mp}만큼 모자랍니다']
        else:
            self.mp -= mp_consum
            damage = random.randint(int(self.power), int(self.power*1.5))
            other.hp = max(other.hp - damage, 0)
            # 데미지의 20% 회복
            heal = int(damage * 0.2)

            self.hp += heal
            # 체력 제한
            if self.max_hp < self.hp:
                self.hp = self.max_hp
            text = [
                f'{self.name}이 마나 {mp_consum}을 소모합니다.\n'
                f"{self.name}의 흡혈 공격!  {other.name}에게 {damage}의 데미지를 입혔습니다.\n"
                f'{self.name}이 체력을{heal} 만큼 회복했습니다.\n'
                f'{self.name}의 현재 HP: {self.hp}\n'
                f'{other.name}의 현재 HP:{other.hp}']
            if other.hp == 0:
                text.append(f"{other.name}이(가) 쓰러졌습니다.")
                self.gold += other.gold
                text.append(f'{self.name}은(는) {other.gold}골드를 얻었습니다.')
        return text

    def wizard_skil_1(self):
        # 마나 회복 : 명상
        mp_recovery = random.randint(1, self.magic_power)
        self.mp += mp_recovery
        # 마나량 제한
        if self.max_mp < self.mp:
            self.mp = self.max_mp

        text = [
            f'{self.name}의 명상! {self.name}이(가) {mp_recovery}만큼 회복하였습니다.\n'
            f'{self.name}의 현재 MP:{self.mp}']
        return text

    def thief_skil_1(self):
        # 회복 : 붕대 감기
        mp_consum = 5
        if self.mp < mp_consum:
            text = [f'마나가{mp_consum - self.mp}만큼 모자랍니다']
        else:
            self.mp -= mp_consum
            heal = random.randint(int(self.avoid*0.5), self.avoid)
            self.hp += heal
            # 체력 제한
            if self.max_hp < self.hp:
                self.hp = self.max_hp
            text = [
                f'{self.name}이 마나 {mp_consum}을 소모합니다.\n'
                f'{self.name}의 붕대 감기 ! {self.name}이(가) {heal}만큼 회복하였습니다.\n'
                f'{self.name}의 현재 HP:{self.hp}']
        return text

    def archer_skil_1(self, other):
        # 타수 스킬
        mp_consum = 5
        if self.mp < mp_consum:
            text = [f'마나가{mp_consum - self.mp}만큼 모자랍니다']
        else:
            self.mp -= mp_consum
            attack_number = random.randint(1, 5)
            damage = random.randint(
                int((self.power+self.magic_power)/2), int((self.power+self.magic_power)))
            other.hp = max(other.hp - damage, 0)
            max_damage = 0
            # 공격 횟수 * damage
            for i in range(1, attack_number+1):
                max_damage += damage
            text = [
                f'{self.name}이 마나 {mp_consum}을 소모합니다.\n'
                f"{self.name}의 연속 공격! {attack_number}번 공격해 {other.name}에게 총 {max_damage}의 데미지를 입혔습니다.\n"
                f'{other.name}의 현재 HP:{other.hp}']
            if other.hp == 0:
                text.append(f"{other.name}이(가) 쓰러졌습니다.")
                self.gold += other.gold
                text.append(f'{self.name}은(는) {other.gold}골드를 얻었습니다.')
        return text


class Item(BaseCharactor):
    def __init__(self, name=None, lv=0, hp=0, mp=0, power=0, magic_power=0, avoid=0):
        super().__init__(name, lv, hp, mp, power, magic_power, avoid)


sub_random = random.randint(1, 3)
main_random = random.randint(3, 5)


item_list = {
    1: Item(name='마법사의 정수', mp=sub_random, magic_power=main_random),
    2: Item(name='전사의 정수', hp=sub_random, power=main_random),
    3: Item(name='도적의 정수', power=sub_random, avoid=main_random),
    4: Item(name='궁수의 정수', hp=main_random, avoid=sub_random),
}


class Inventory(BaseCharactor):
    def __init__(self, name=None, lv=None, hp=None, mp=None, power=None, magic_power=None, avoid=None, gold=None):
        super().__init__(name, lv, hp, mp, power, magic_power, avoid)
        self.gold = gold


# gold 조정해야함
shopping_list = {
    1: Inventory(name='hp potion', hp=10, gold=50),
    2: Inventory(name='mp potion', mp=5, gold=80),
    3: Inventory(name='power +10 up', power=10, gold=100),
    4: Inventory(name='magic power +10 up', magic_power=10, gold=120),
}
