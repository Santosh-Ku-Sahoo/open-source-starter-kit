# Problem: Valid Parentheses
# Difficulty: Easy
# Approach: Stack-based matching of opening and closing brackets
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Problem Statement:
# Given a string containing only the characters '(', ')', '{', '}',
# '[' and ']', determine if the input string has valid (balanced)
# parentheses. Every opening bracket must have a matching closing
# bracket in the correct order.

def valid_parentheses(s):
    """
    Checks if the input string has balanced parentheses using a stack.
    Supports (), [], and {} bracket pairs.

    Args:
        s: String containing bracket characters.

    Returns:
        True if all brackets are properly balanced, False otherwise.
    """
    stack = []
    bracket_map = {")": "(", "]": "[", "}": "{"}

    for char in s:
        if char in bracket_map.values():
            # Opening bracket — push onto stack
            stack.append(char)
        elif char in bracket_map:
            # Closing bracket — check for matching opening
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()

    # Stack should be empty if all brackets matched
    return len(stack) == 0


# ---- Test Cases ----
if __name__ == "__main__":
    print(valid_parentheses("()"))          # Expected: True
    print(valid_parentheses("()[]{}"))      # Expected: True
    print(valid_parentheses("(]"))          # Expected: False
    print(valid_parentheses("([)]"))        # Expected: False
    print(valid_parentheses("{[]}"))        # Expected: True
    print(valid_parentheses(""))            # Expected: True
    print(valid_parentheses("((()))"))      # Expected: True
    print(valid_parentheses("("))           # Expected: False
    print(valid_parentheses(")"))           # Expected: False
    print(valid_parentheses("{[()]}"))      # Expected: True
