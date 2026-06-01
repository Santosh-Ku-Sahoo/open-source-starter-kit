# Problem: Find Max and Min in an Array
# Difficulty: Easy
# Approach: Single pass tracking both max and min
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Problem Statement:
# Given an array of numbers, find both the maximum and minimum values
# in a single pass. Handle edge cases like empty arrays and single elements.

def find_max_min(arr):
    """
    Finds the maximum and minimum values in the array using a single pass.

    Args:
        arr: List of numbers.

    Returns:
        A tuple (max_val, min_val). Returns (None, None) for empty arrays.
    """
    if not arr:
        return (None, None)

    max_val = arr[0]
    min_val = arr[0]

    for num in arr[1:]:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num

    return (max_val, min_val)


# ---- Test Cases ----
if __name__ == "__main__":
    print(find_max_min([3, 5, 1, 8, 2]))        # Expected: (8, 1)
    print(find_max_min([10]))                    # Expected: (10, 10)
    print(find_max_min([]))                      # Expected: (None, None)
    print(find_max_min([-5, -1, -8, -3]))        # Expected: (-1, -8)
    print(find_max_min([7, 7, 7, 7]))            # Expected: (7, 7)
    print(find_max_min([1, 2, 3, 4, 5]))         # Expected: (5, 1)
    print(find_max_min([5, 4, 3, 2, 1]))         # Expected: (5, 1)
    print(find_max_min([-10, 0, 10, -20, 20]))   # Expected: (20, -20)
