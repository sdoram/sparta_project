import random
# 직업
# 직업 스킬


class Job():

    def job_select():
        job_dict = {
            '1': {
                'job': '전사',
                'hp': 300,
                'mp': 200,
                'power': 20,
                'magic_power': 10,
                'avoid': 10,
                'gold': 0
            },
            '2': {
                'job': '마법사',
                'hp': 100,
                'mp': 200,
                'power': 10,
                'magic_power': 30,
                'avoid': 10,
                'gold': 5
            },
            '3': {
                'job': '궁수',
                'hp': 150,
                'mp': 100,
                'power': 15,
                'magic_power': 20,
                'avoid': 10,
                'gold': 10
            },
            '4': {
                'job': '도적',
                'hp': 150,
                'mp': 100,
                'power': 20,
                'magic_power': 15,
                'avoid': 40,
                'gold': 30
            },
        }
        while True:
            print('전사:1 마법사:2 궁수:3 도적:4')
            job_input = input('직업을 선택해주세요 : ')
            if job_input in job_dict.keys():
                # print(job_dict[job_input].values())
                break
            else:
                print('올바른 입력 값 X')
                continue
        return job_dict[job_input]


# class Warrior:
#     def warrior_skil_1(self, other):
#         mana_consum = 5
#         if self.mana < mana_consum:
#             print('마나가 모자랍니다')
#         else:
#             self.mana -= mana_consum
#             damage = random.randint(self.magic_power, self.magic_power + 5)
#             other.hp = max(other.hp - damage, 0)
#             print(
#                 f'마나 {mana_consum}을 소모합니다.\n'
#                 f"{self.name}의 마법 공격!  {other.name}에게 {damage}의 데미지를 입혔습니다.\n"
#                 f'{other.name}의 현재 HP:{other.hp}')
#             if other.hp == 0:
#                 print(f"{other.name}이(가) 쓰러졌습니다.")


# class Wizrad:
#     def thief_skil_1(self, other):
#         mana_consum = 5
#         if self.mana < mana_consum:
#             print('마나가 모자랍니다')
#         else:
#             self.mana -= mana_consum
#             damage = random.randint(self.magic_power, self.magic_power + 5)
#             other.hp = max(other.hp - damage, 0)
#             print(
#                 f'마나 {mana_consum}을 소모합니다.\n'
#                 f"{self.name}의 마법 공격!  {other.name}에게 {damage}의 데미지를 입혔습니다.\n"
#                 f'{other.name}의 현재 HP:{other.hp}')
#             if other.hp == 0:
#                 print(f"{other.name}이(가) 쓰러졌습니다.")


# class Thief:
#     def thief_skil_1(self, other):
#         mana_consum = 5
#         if self.mana < mana_consum:
#             print('마나가 모자랍니다')
#         else:
#             self.mana -= mana_consum
#             damage = random.randint(self.magic_power, self.magic_power + 5)
#             other.hp = max(other.hp - damage, 0)
#             print(
#                 f'마나 {mana_consum}을 소모합니다.\n'
#                 f"{self.name}의 마법 공격!  {other.name}에게 {damage}의 데미지를 입혔습니다.\n"
#                 f'{other.name}의 현재 HP:{other.hp}')
#             if other.hp == 0:
#                 print(f"{other.name}이(가) 쓰러졌습니다.")


# class Archer:
#     def archer_skil_1(self, other):
#         mana_consum = 5
#         if self.mana < mana_consum:
#             print('마나가 모자랍니다')
#         else:
#             self.mana -= mana_consum
#             damage = random.randint(self.magic_power, self.magic_power + 5)
#             other.hp = max(other.hp - damage, 0)
#             print(
#                 f'마나 {mana_consum}을 소모합니다.\n'
#                 f"{self.name}의 마법 공격!  {other.name}에게 {damage}의 데미지를 입혔습니다.\n"
#                 f'{other.name}의 현재 HP:{other.hp}')
#             if other.hp == 0:
#                 print(f"{other.name}이(가) 쓰러졌습니다.")
if __name__ == "__main__":
    Job.job_select()
