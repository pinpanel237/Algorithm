def solution(wallet, bill):
    answer = 0
    
    while True:
        if check_size(wallet, bill):
            return answer
        else:
            if bill[0] < bill[1]:
                bill = [bill[0], bill[1] // 2]
            else:
                bill = [bill[0] // 2, bill[1]]
        answer += 1
    
    return answer

def check_size(wallet, bill):
    if bill[0] <= wallet[0] and bill[1] <= wallet[1]:
        return True
    elif bill[1] <= wallet[0] and bill[0] <= wallet[1]:
        return True
    return False