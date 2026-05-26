# Problem: Palindrome Check
# Difficulty: Easy
# Approach: Two-Pointer, Slicing, Recursive
# Time Complexity: O(n) for all approaches
# Space Complexity: O(n) for slicing/recursive, O(1) for two-pointer
#
# Problem Statement:
# Given a string, determine if it is a palindrome. Consider only
# alphanumeric characters and ignore case sensitivity.


def is_palindrome_two_pointer(s):
    """
    Check palindrome using two pointers moving inward.
    Skips non-alphanumeric characters and ignores case.
    """
    left, right = 0, len(s) - 1

    while left < right:
        # Skip non-alphanumeric characters from the left
        while left < right and not s[left].isalnum():
            left += 1
        # Skip non-alphanumeric characters from the right
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


def is_palindrome_slice(s):
    """
    Check palindrome by filtering and comparing with reversed slice.
    Cleans the string first, then uses slicing to reverse.
    """
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]


def is_palindrome_recursive(s):
    """
    Check palindrome using recursion on a cleaned string.
    Base case: string of length 0 or 1 is a palindrome.
    """
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())

    def helper(text, left, right):
        if left >= right:
            return True
        if text[left] != text[right]:
            return False
        return helper(text, left + 1, right - 1)

    return helper(cleaned, 0, len(cleaned) - 1)


# ---- Test Cases ----
if __name__ == "__main__":
    test_cases = [
        ("racecar", True),
        ("hello", False),
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("", True),                    # empty string
        ("a", True),                   # single character
        ("Madam", True),               # mixed case palindrome
        ("Was it a car or a cat I saw?", True),
        ("No lemon, no melon", True),
        ("12321", True),               # numeric palindrome
        ("12345", False),
    ]

    approaches = [
        ("Two-Pointer", is_palindrome_two_pointer),
        ("Slicing", is_palindrome_slice),
        ("Recursive", is_palindrome_recursive),
    ]

    for name, func in approaches:
        print(f"--- {name} Approach ---")
        all_passed = True
        for input_str, expected in test_cases:
            result = func(input_str)
            status = "PASS" if result == expected else "FAIL"
            if status == "FAIL":
                all_passed = False
            print(f"  is_palindrome({input_str!r}) = {result}  [{status}]")
        print(f"  All tests passed: {all_passed}\n")
