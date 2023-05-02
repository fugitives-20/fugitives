import random

def generate_secret_code():
    """
    1에서 9까지 서로 다른 숫자 4개로 이루어진 비밀 코드를 생성합니다.
    """
    numbers = list(range(1, 10))
    random.shuffle(numbers)
    return numbers[:4]

print(generate_secret_code())
