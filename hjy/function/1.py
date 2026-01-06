def greet() -> str:
    return "안녕하세요!"

def print_sum(a: int, b: int) -> None:
    print(f"{a} + {b} = {a + b}")

def noop() -> None:
    print("그냥 실행만 합니다(반환 없음).")

def double(x: int) -> int:
    return x * 2

if __name__ == "__main__":
    msg = greet()          # 입력 X, 반환 O
    print(msg)

    print_sum(3, 4)        # 입력 O, 반환 X
    noop()                 # 입력 X, 반환 X
    print(double(10))      # 입력 O, 반환 O
