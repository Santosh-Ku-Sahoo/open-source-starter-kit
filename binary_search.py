# Problem: Binary Search
# Difficulty: Easy
# Approach: Divide and conquer — iterative and recursive
# Time Complexity: O(log n)
# Space Complexity: O(1) iterative, O(log n) recursive (call stack)
#
# Problem Statement:
# Given a sorted array of integers and a target value, return the index
# of the target if found, or -1 if not found. Implement both iterative
# and recursive approaches.

def binary_search_iterative(arr, target):
    """
    Iterative binary search.
    Searches for target in a sorted array by repeatedly halving
    the search space.

    Args:
        arr: Sorted list of integers.
        target: Value to search for.

    Returns:
        Index of target if found, -1 otherwise.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # avoids integer overflow

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def binary_search_recursive(arr, target, left=0, right=None):
    """
    Recursive binary search.
    Divides the search space in half with each recursive call.

    Args:
        arr: Sorted list of integers.
        target: Value to search for.
        left: Left boundary index (default 0).
        right: Right boundary index (default len(arr) - 1).

    Returns:
        Index of target if found, -1 otherwise.
    """
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1

    mid = left + (right - left) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


# ---- Test Cases ----
if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13, 15]

    print("--- Iterative Binary Search ---")
    print(binary_search_iterative(arr, 7))     # Expected: 3
    print(binary_search_iterative(arr, 1))     # Expected: 0
    print(binary_search_iterative(arr, 15))    # Expected: 7
    print(binary_search_iterative(arr, 6))     # Expected: -1
    print(binary_search_iterative([], 5))      # Expected: -1

    print("\n--- Recursive Binary Search ---")
    print(binary_search_recursive(arr, 7))     # Expected: 3
    print(binary_search_recursive(arr, 1))     # Expected: 0
    print(binary_search_recursive(arr, 15))    # Expected: 7
    print(binary_search_recursive(arr, 6))     # Expected: -1
    print(binary_search_recursive([], 5))      # Expected: -1
