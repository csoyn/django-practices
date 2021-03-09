from django.shortcuts import render
import random
import requests

def lotto(request):
    url = 'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=927'

    response = requests.get(url).json()
    print(type(response))
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

    return render(request, 'lotto.html', context)
