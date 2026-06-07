def solution(message, spoiler_ranges):
    message_list = list(message)
    
    for start, end in spoiler_ranges:
        for i in range(start, end + 1):
            if message_list[i] != ' ':
                message_list[i] = '@'
        
    masked_message = ''.join(message_list)
    original_words = message.split()
    masked_words = masked_message.split()
    spoiler_words = set()
            
    for o_word, m_word in zip(original_words, masked_words):
        if '@' in m_word:
            spoiler_words.add(o_word)
    
    masked_words_set = set(masked_words)
    answer = len(spoiler_words)
    for sw in spoiler_words:
        if sw in masked_words_set:
            answer -= 1
    
    return answer