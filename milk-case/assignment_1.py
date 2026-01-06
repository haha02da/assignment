import sys

while(True):        
    stack = []
    flg = True

    test_str = sys.stdin.readline().rstrip()

    if test_str == 'exit':
        print('process exit')
        break

    for char in test_str:
        if char == '(' or char == '{':
            stack.append('(')
        elif char == ')' or char == '}':
            if len(stack) == 0:
                print("syntax error")
                flg = False
            else:
                stack.pop()
    if flg:
        print("correct")