from itertools import combinations

def solution(n, q, ans):
    answer = 0
    
    all_cases = list(combinations(range(1, n + 1), 5))

    for q_i, ans_i in zip(q, ans):
        q_set = set(q_i)
        inc_list = list(combinations(q_i, ans_i))
        new_cases = []
        
        for c in all_cases:
            for inc_i in inc_list:
                inc_set = set(inc_i)
                c_set = set(c)
                if inc_set.issubset(c_set) and not set(q_set - inc_set).intersection(c_set):
                    new_cases.append(c)
                    
        all_cases = new_cases
        
    return len(all_cases)