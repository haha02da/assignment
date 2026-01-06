import sys

flg = True

def is_balanced_brackets(s: str):
    if s == 'exit':
        return -1
    
    open = ['(', '{', '[']
    close = [')', '}', ']']
    stack = []
    
    for char in s:
        if char in open:
            stack.append(char)
        elif char in close:
            if not stack or stack[-1] != open[(close.index(char))]:
                return False
            stack.pop()
    
    return (not stack)

while(flg):
    print('Enter String : ')
    res = is_balanced_brackets(sys.stdin.readline().rstrip())
    
    if res == -1:
        flg = False
    else:
        print(res)    