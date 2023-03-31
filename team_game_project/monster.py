from charactor import *
import random


class Monster(BaseCharactor):
    def __init__(self, name, lv, hp, mp, power, magic_power, avoid):
        super().__init__(name, lv, hp, mp, power, magic_power, avoid)
         

class Slime(Monster):
    def __init__(self, lv):
        self.name = 'Slime'
        self.lv = lv
        self.max_hp = 100 + (lv * 5)
        self.hp = self.max_hp
        self.max_mp = 3 + lv
        self.mp = self.max_mp
        self.power = random.randint(2, 7) + lv
        self.magic_power = 10 + lv
        self.avoid = 10 + lv
        self.attack_type = 1
        self.gold = random.randint(100-lv*10, 100+lv*10)

    def random_attack(self, other):
        # 마나 체크 후 공격 타입 지정
        if self.mp>=5:
            self.attack_type = random.randint(1, 2)
        else: self.attack_type ==1
        if self.attack_type == 1:
            return self.attack(other)
        else :
            return self.power_attack(other)


class Skeleton(Monster):
    def __init__(self, lv):
        self.name = 'Skeleton'
        self.lv = lv
        self.max_hp = 120 + (lv*10)
        self.hp = self.max_hp
        self.max_mp = 7 + lv
        self.mp = self.max_mp
        self.power = random.randint(5, 10) + lv
        self.magic_power = 20 + lv
        self.avoid = 5 + lv
        self.attack_type = 3
        self.gold = random.randint(100-lv*10, 100+lv*10)

    def bone_magic(self, other):
        mp_consum=5
        self.mp -= mp_consum
        damage = random.randint(self.power+3, self.magic_power+self.power)
        other.hp = max(other.hp - damage, 0)
        text = [
        f'{self.name}이 마나 {mp_consum}을 소모합니다.\n'
        f'{self.name}의 뼈 마법!  {other.name}에게 {damage}의 데미지를 입혔습니다.\n'
        f'{other.name}의 현재 HP:{other.hp}']
        if other.hp == 0:
            text = f"{other.name}이(가) 쓰러졌습니다."
        return text

    def random_attack(self, other):
        # 마나 체크 후 공격 타입 지정
        if self.mp == self.max_mp:
            self.attack_type = 3
        else:
            if self.mp>5: 
                self.attack_type = random.randint(1, 2)
            else : self.attack_type = 1
        if self.attack_type == 1:
            return self.attack(other)
        elif self.attack_type == 2:
            return self.power_attack(other)
        else:
            return self.bone_magic(other)


class Zombie(Monster):
    def __init__(self, lv):
        self.name = 'Zombie'
        self.lv = lv
        self.max_hp = 200 + (lv*10)
        self.hp = random.randint(100,self.max_hp)
        self.max_mp = 10 + lv
        self.mp = self.max_mp
        self.power = random.randint(10, 15) + lv
        self.magic_power = 5 +lv
        self.avoid = 1 + lv
        self.attack_type = 3
        self.gold = random.randint(100-lv*10, 100+lv*10)

    def recovery(self):
        mp_consum=5
        self.mp -= mp_consum
        # self.mp -= 5
        # 턴 수 * 2로 회복
        recovery = self.lv*2
        self.hp += recovery
        if self.max_hp < self.hp:
            self.hp = self.max_hp
        text = [f'{self.name}이 마나 {mp_consum}을 소모합니다.\n'
        f'{self.name}의 회복! {self.name}이(가) {recovery}만큼 회복하였습니다.\n'
        f'{self.name}의 현재 HP:{self.hp}\n']
        return text

    def random_attack(self, other):
        # 마나 체크 후 공격 타입 지정
        mp_consum=5
        if self.mp == mp_consum:
            self.attack_type = 3
        else:
            if self.mp>5: 
                self.attack_type = random.randint(1, 2)
            else : self.attack_type = 1
        if self.attack_type == 1:
            return self.attack(other)
        elif self.attack_type == 2:
            return self.power_attack(other)
        else:
            return self.recovery()


# monster_list = [Slime(), Skeleton(), Zombie()]
# # 랜덤 몬스터 생성
# monster = random.choice(monster_list)
