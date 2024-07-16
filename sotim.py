from collections import deque
def is_valid(s):
    balance = 0
    for char in s:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        if balance < 0:
            return False
    return balance == 0

def remove_invalid_parentheses(s):
    if not s:
        return [""]
    visited = set()
    queue = deque([s])
    found = False
    valid_expressions = []

    while queue:
        level_size = len(queue)
        current_level = set()
        for _ in range(level_size):
            current_string = queue.popleft()
            if is_valid(current_string):
                valid_expressions.append(current_string)
                found = True
            if found:
                continue
            for i in range(len(current_string)):
                if current_string[i] not in ('(', ')'):
                    continue
                next_state = current_string[:i] + current_string[i + 1:]
                if next_state not in visited:
                    visited.add(next_state)
                    current_level.add(next_state)
        if found:
            break
        queue.extend(current_level)

    return valid_expressions

input_str = input("Enter the parentheses string: ")

output = remove_invalid_parentheses(input_str)
print("Valid parentheses strings:", output)