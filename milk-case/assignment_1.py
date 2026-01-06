import sys

def is_balanced_parentheses(s:str):      
    stack = []

    if s == 'exit':
        print('<<process exit>>')
        return -1

    for char in s:
        if char == '(':
            stack.append('(')
        elif char == ')':
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    
    return (not stack)

flg = True

while(flg):
    print('Enter String : ')
    res = is_balanced_parentheses(sys.stdin.readline().rstrip())

    if res == -1:
        flg = False
    else:
        print(res)