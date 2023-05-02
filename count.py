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
