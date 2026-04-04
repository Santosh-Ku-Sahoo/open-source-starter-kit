# Problem: Two Sum
# Difficulty: Easy
# Approach: HashMap (single pass)
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Problem Statement:
# Given an array of integers and a target, return indices of
# the two numbers that add up to the target.

def two_sum(nums, target):
    """
    Uses a hashmap to store complement of each number.
    For each number, check if its complement already exists.
    """
    seen = {}  # value -> index

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return []  # no solution found


# ---- Test Cases ----
if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))   # Expected: [0, 1]
    print(two_sum([3, 2, 4], 6))         # Expected: [1, 2]
    print(two_sum([3, 3], 6))            # Expected: [0, 1]
