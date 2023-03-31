import random, time
from script import *


def call_sphinx():
    quiz = ['sophisticated', 'formerly', 'sophistication', 'conveniently', 'consecutive', 'convenient', 'consecutively', 'increase', 'quality', 'decrease', 'completely', 'consistency', 'complete', 'inconsistency', 'completion', 'enhance', 'information', 'establish', 'deliberation', 'estimate', 'impressive', 'renovate', 'impression', 'renovation', 'trensfer', 'arise', 'reduce', 'recommend', 'beware', 'recommendation', 'innate', 'collateral', 'restore', 'personality', 'necessary', 'appearance', 'health', 'certain', 'healthy', 'uncertain', 'delicate', 'excessive', 'disturb', 'exceed', 'speculate', 'excellent',
            'speculation', 'delegate', 'scenery', 'direct', 'consist', 'direction', 'consistent', 'circumscribe', 'deficit', 'prohibit', 'symptom', 'prohibition', 'budget', 'innovate', 'preserve', 'innovation', 'calculate', 'safety', 'calculation', 'produce', 'assent', 'production', 'significant', 'refuse', 'exhibit', 'expend', 'exhibition', 'require', 'assert', 'contribute', 'competent', 'coordinate', 'incompetent', 'coordination', 'insurance', 'instruct', 'mandatory', 'instruction', 'frequently', 'amend', 'frequency', 'inquire', 'retire', 'occupy', 'retirement', 'garner', 'pedestrian', 'monetary', 'abuse', 'financial']

    # 랜덤 뽑기 choice
    word = random.choice(quiz)

    # 유저가 입력하는 문자열
    answer = ''

    # 기회
    count = 18

    print_writting = '_'*(len(word))

    time.sleep(1)
    typing('스핑크스가 출현했습니다.')
    time.sleep(1.5)
    typing(f'스핑크스가 내는 문제를 맞추세요.')
    time.sleep(1)

    while count > 0:

        time.sleep(0.5)
        typing(f'기회는 {count}번 남았습니다.')

        if answer == '':
            user_put = input(print_writting + ' : ').lower()
            for w in list(word):  # 처음에는 answer에 문자열 다 넣기
                if w == user_put:
                    answer += w
                else:
                    answer += '_'

        else:
            time.sleep(0.5)
            user_put = input(answer + ' : ').lower()

            for idx, w in enumerate(list(word)):  # 두 번째 부터 정답인 문자만 교체
                if w == user_put:
                    a = list(answer)  #
                    a[idx] = w
                    answer = ''.join(a)

        count -= 1

        # 리스트 인덱스 값과 상관없이 같은 문자를 가지면 종료
        if sorted(answer) == sorted(word):
            typing(f'{answer} 정답입니다.')
            break

    # 기회 안에 못 풀면 빠꾸시키기
    if count == 0:
        typing('틀렸어요')

    return
    # 에러
    # TypeError: 'str' object does not support item assignment
    # 임의의 문자열 print_writting의 인덱스로 w 문자열 삽입이 안됨
    # print_writting 값을 변화주는게 어려웠음
