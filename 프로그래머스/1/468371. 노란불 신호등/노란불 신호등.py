import math

def solution(signals):
    answer = 1
    s_list = [[] for _ in signals]
    
    for index, s in enumerate(signals):
        for i in range(3):
            s_list[index].extend([True if i == 1 else False for _ in range(s[i])])
    
    s_sum = [sum(s) for s in signals]
    limit = s_sum[0]
    for ss in s_sum[1:]:
        limit = get_lcm(limit, ss)
    
    while answer <= limit:
        result = True
        
        for s in s_list:
            result &= s[answer % len(s)]
        
        if result:
            return answer + 1
        else:
            answer += 1
    
    return -1

def get_lcm(a, b):
    return (a * b) // math.gcd(a, b)