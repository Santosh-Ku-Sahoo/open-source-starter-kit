# Problem: Count Vowels in a String
# Difficulty: Easy
# Approach: Single pass with set lookup
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Problem Statement:
# Given a string, count the number of vowels (a, e, i, o, u).
# Handle both uppercase and lowercase characters.

def count_vowels(s):
    """
    Counts the number of vowels in the given string.
    Handles both uppercase and lowercase vowels.

    Args:
        s: Input string.

    Returns:
        Integer count of vowels found in the string.
    """
    vowels = set("aeiouAEIOU")
    count = 0

    for char in s:
        if char in vowels:
            count += 1

    return count


# ---- Test Cases ----
if __name__ == "__main__":
    print(count_vowels("hello"))              # Expected: 2
    print(count_vowels("HELLO"))              # Expected: 2
    print(count_vowels("HeLLo WoRLd"))        # Expected: 3
    print(count_vowels("aeiou"))              # Expected: 5
    print(count_vowels("AEIOU"))              # Expected: 5
    print(count_vowels("bcdfg"))              # Expected: 0
    print(count_vowels(""))                   # Expected: 0
    print(count_vowels("Python Programming")) # Expected: 4
