def solution(keymap, targets):
    answer = []
    keys = {}
    
    for key in keymap:
        for idx, c in enumerate(key):
            if c in keys:
                keys[c] = idx + 1 if idx + 1 < keys[c] else keys[c]
            else:
                keys[c] = idx + 1
    
    for target in targets:
        result = 0
        
        for c in target:
            if c in keys:
                result += keys[c]
            else:
                result = 0
                break
                
        answer.append(result if result != 0 else -1)
        
    return answer