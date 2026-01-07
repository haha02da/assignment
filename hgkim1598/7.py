import random

com_answer = random.randrange(1, 20, 1)

user_answer = 0

def check_answer():
  if user_answer > com_answer:
    print("DOWN")
    return False
  elif user_answer < com_answer:
    print("UP")
    return False
  else:
    print(f"정답! {com_answer}")
    return True

for i in range(5):
  user_answer = int(input("숫자를 입력해주세요:"))
  result = check_answer()
  if result:
    break
else:
  print("실패")
