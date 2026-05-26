# Problem: Longest Common Subsequence (LCS)
# Difficulty: Intermediate
# Approach: Dynamic Programming with 2D table and backtracking
# Time Complexity: O(m * n) where m, n are lengths of the two strings
# Space Complexity: O(m * n) for the DP table
#
# Problem Statement:
# Given two strings, find the length of their longest common subsequence
# and also reconstruct the LCS string itself.

def longest_common_subsequence(text1, text2):
    """
    Finds the length and the actual longest common subsequence of two strings
    using dynamic programming.

    Args:
        text1: First input string.
        text2: Second input string.

    Returns:
        A tuple (length, lcs_string) where length is the LCS length
        and lcs_string is one possible LCS.
    """
    m, n = len(text1), len(text2)

    # Build the DP table
    # dp[i][j] = length of LCS of text1[:i] and text2[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Backtrack to find the actual LCS string
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if text1[i - 1] == text2[j - 1]:
            lcs.append(text1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    lcs.reverse()
    lcs_string = "".join(lcs)

    return (dp[m][n], lcs_string)


# ---- Test Cases ----
if __name__ == "__main__":
    length, lcs = longest_common_subsequence("abcde", "ace")
    print(f"LCS length: {length}, LCS: '{lcs}'")  # Expected: 3, 'ace'

    length, lcs = longest_common_subsequence("abc", "abc")
    print(f"LCS length: {length}, LCS: '{lcs}'")  # Expected: 3, 'abc'

    length, lcs = longest_common_subsequence("abc", "def")
    print(f"LCS length: {length}, LCS: '{lcs}'")  # Expected: 0, ''

    length, lcs = longest_common_subsequence("AGGTAB", "GXTXAYB")
    print(f"LCS length: {length}, LCS: '{lcs}'")  # Expected: 4, 'GTAB'

    length, lcs = longest_common_subsequence("", "abc")
    print(f"LCS length: {length}, LCS: '{lcs}'")  # Expected: 0, ''

    length, lcs = longest_common_subsequence("abcdef", "fbdamn")
    print(f"LCS length: {length}, LCS: '{lcs}'")  # Expected: 2, 'bd'
