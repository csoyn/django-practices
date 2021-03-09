from django.shortcuts import render
import random
import requests

# 민환
def lotto(request):
    url = 'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=927'

    response = requests.get(url).json()
    
    # 두호
    '''
    numbers = []
    for i in range(1, 7):
        numbers.append(response.get(f'drwtNo{i}'))
    bonus_number = response.get('bnusNo')
    result = [0] * 6
    for _ in range(1000):
        temp = random.sample(range(1, 46), 6)

        temp_count = 0

        for temp_num in temp:
            if temp_num in numbers:
                temp_count += 1

        if temp_count == 6:
            result[0] += 1
        elif temp_count == 5 and bonus_number in temp:
            result[1] += 1
        elif temp_count == 5:
            result[2] += 1
        elif temp_count == 4:
            result[3] += 1
        elif temp_count == 3:
            result[4] += 1
        else:
            result[5] += 1
    context = {
        'numbers': numbers,
        'bonus_number': bonus_number,
        'result': result,
    }
    '''

    # 근일
    winnings = [response.get(f'drwtNo{i}') for i in range(1, 7)]
    bonus_number = response.get('bnusNo')
    random_numbers = [random.sample(range(1, 46), 6) for _ in range(1000)]

    winning_sup = {
        '1등': 0,
        '2등': 0,
        '3등': 0,
        '4등': 0,
        '5등': 0,
        '꽝': 0,
    }

    for target_numbers in random_numbers:
        cnt = 0
        for i in range(6):
            if target_numbers[i] in winnings:
                cnt += 1

        if cnt == 6:
            winning_sup['1등'] += 1
        elif cnt == 5:
            if bonus_number in target_numbers:
                winning_sup['2등'] += 1
            else:
                winning_sup['3등'] += 1
        elif cnt == 4:
            winning_sup['4등'] += 1
        elif cnt == 3:
            winning_sup['5등'] += 1
        else:
            winning_sup['꽝'] += 1

    context = {
        'winnings': winnings,
        'bonus_number': bonus_number,
        'winning_sup': winning_sup,
    }

    return render(request, 'lotto.html', context)
