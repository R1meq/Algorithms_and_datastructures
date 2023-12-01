def get_next_state(pattern, pattern_length, current_state, current_char):
    if current_state < pattern_length and current_char == ord(pattern[current_state]):
        return current_state + 1

    i = 0
    for next_state in range(current_state, 0, -1):
        if ord(pattern[next_state - 1]) == current_char:
            while i < next_state - 1:
                if pattern[i] != pattern[current_state - next_state + 1 + i]:
                    break
                i += 1
            if i == next_state - 1:
                return next_state

    return 0


def build_finite_automaton_table(pattern, pattern_length):
    tf_table = [[0 for _ in range(128)] for _ in range(pattern_length + 1)]
    for state in range(pattern_length + 1):
        for char_code in range(128):
            next_state = get_next_state(pattern, pattern_length, state, char_code)
            tf_table[state][char_code] = next_state
    return tf_table

def search_pattern_in_text(pattern, text):
    pattern_length = len(pattern)
    text_length = len(text)
    tf_table = build_finite_automaton_table(pattern, pattern_length)
    result = []

    state = 0
    for current_character in range(text_length):
        state = tf_table[state][ord(text[current_character])]
        if state == pattern_length:
            result.append(current_character - pattern_length + 1)

    return result