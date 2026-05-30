def is_valid_parentheses(s: str) -> bool:
    """
    Return True if the string contains valid, balanced parentheses.
    Only (), {}, and [] are considered valid.
    """
    pairs = {")": "(", "}": "{", "]": "["}
    openings = set(pairs.values())
    stack = []

    for char in s:
        if char in openings:
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False

    return not stack
