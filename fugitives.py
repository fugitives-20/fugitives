import random
def generate_secret_code():
    """
    1에서 9까지 서로 다른 숫자 4개로 이루어진 비밀 코드를 생성합니다.
    """
    numbers = list(range(1, 10))
    random.shuffle(numbers)
    return numbers[:4]

def count_bulls_and_cows(secret_code, guess):
    """
    비밀 코드와 추측한 숫자를 비교하여 불과 카우의 개수를 계산합니다.
    """
    bulls, cows = 0, 0
    for i in range(4):
        if guess[i] == secret_code[i]:
            bulls += 1
        elif guess[i] in secret_code:
            cows += 1
    return bulls, cows
