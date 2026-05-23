def solution(n):
    answer = 0
    mul_num = 1
    stack = []
    
    while n != 0:
        stack.append(n % 3)
        n //= 3
    
    while stack:
        answer += stack.pop()  * mul_num
        mul_num *= 3
        
    return answer