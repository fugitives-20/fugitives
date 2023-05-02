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
# 게임 시작
secret_code = generate_secret_code()
print("불스 앤 카우스 게임을 시작합니다. 1에서 9까지 서로 다른 숫자 4개를 맞춰보세요.")
num_attempts = 0
while num_attempts < 10:
    num_attempts += 1
    guess = input(f"{num_attempts}번째 추측: ")
    guess = [int(n) for n in guess if n.isdigit()]
    if len(guess) != 4 or len(set(guess)) != 4:
        print("잘못된 입력입니다. 1에서 9까지 서로 다른 숫자 4개를 입력해주세요.")
        continue
    bulls, cows = count_bulls_and_cows(secret_code, guess)
    print(f"{bulls} 불, {cows} 카우")
    if bulls == 4:
        print("축하합니다! 비밀 코드를 맞추셨습니다.")
        break
else:
    print("게임 오버! 10번의 시도 기회를 모두 사용하셨습니다. 비밀 코드는", secret_code, "였습니다.")
