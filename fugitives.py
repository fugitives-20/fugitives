## 함수 만들기, 구현 연습

def main():
    while True:
        print("\nBulls and Cows 게임을 시작합니다.")
        ans = gen_game()
        tries, endmsg = 1, f"Game Over. 정답: {ans}"
        while tries < 11:
            gss = input("맞춰보세요(4자리 숫자): ")
            if not chk_gss(gss):
                continue
            result, stat = get_result(ans, gss)
            if result == True:
                endmsg = f"정답입니다. 총 입력한 횟수: {tries}"
                break
            else:
                print(f"결과는 {stat}입니다. 총 입력한 횟수: {tries}")
            tries += 1
        print(endmsg)

        while True:
            retry = input("다시 시작할까요([0] 아니오, [1] 예)? ")
            if retry == "0":
                exit()
            elif retry == "1":
                break
            else:
                print("잘못된 입력입니다.")
                continue


if __name__ == "__main__":
    main()

