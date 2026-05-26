# Problem: Reverse a String
# Difficulty: Easy
# Approach: Slicing, Two-Pointer, Recursive
# Time Complexity: O(n) for all approaches
# Space Complexity: O(n) for slicing/recursive, O(1) for two-pointer (in-place)
#
# Problem Statement:
# Given a string, return it reversed. Implement multiple approaches
# and handle edge cases like empty strings and single characters.


def reverse_string_slice(s):
    """
    Reverse a string using Python slicing.
    Simple and Pythonic one-liner.
    """
    return s[::-1]


def reverse_string_two_pointer(s):
    """
    Reverse a string using the two-pointer technique.
    Swaps characters from both ends moving inward.
    """
    chars = list(s)
    left, right = 0, len(chars) - 1

    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

    return "".join(chars)


def reverse_string_recursive(s):
    """
    Reverse a string using recursion.
    Base case: empty string or single character.
    Recursive step: last char + reverse of the rest.
    """
    if len(s) <= 1:
        return s
    return s[-1] + reverse_string_recursive(s[:-1])


# ---- Test Cases ----
if __name__ == "__main__":
    test_cases = [
        ("hello", "olleh"),
        ("world", "dlrow"),
        ("", ""),                  # empty string
        ("a", "a"),                # single character
        ("racecar", "racecar"),    # palindrome stays the same
        ("ab", "ba"),              # two characters
        ("Hello, World!", "!dlroW ,olleH"),  # mixed case & punctuation
    ]

    approaches = [
        ("Slicing", reverse_string_slice),
        ("Two-Pointer", reverse_string_two_pointer),
        ("Recursive", reverse_string_recursive),
    ]

    for name, func in approaches:
        print(f"--- {name} Approach ---")
        all_passed = True
        for input_str, expected in test_cases:
            result = func(input_str)
            status = "PASS" if result == expected else "FAIL"
            if status == "FAIL":
                all_passed = False
            print(f"  reverse({input_str!r}) = {result!r}  [{status}]")
        print(f"  All tests passed: {all_passed}\n")
