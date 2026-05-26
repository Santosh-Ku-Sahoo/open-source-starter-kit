# Problem: Merge Sort
# Difficulty: Intermediate
# Approach: Divide and conquer — split, sort recursively, merge
# Time Complexity: O(n log n) in all cases
# Space Complexity: O(n) — auxiliary space for merging
#
# Problem Statement:
# Sort an array of integers using the merge sort algorithm.
# Divide the array into halves, recursively sort each half,
# then merge the sorted halves back together.

def merge_sort(arr):
    """
    Sorts the array using merge sort (divide and conquer).
    Recursively splits the array in half, sorts each half,
    and merges the sorted halves.

    Args:
        arr: List of comparable elements to sort.

    Returns:
        A new sorted list.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    """
    Merges two sorted lists into a single sorted list.

    Args:
        left: First sorted list.
        right: Second sorted list.

    Returns:
        A merged sorted list.
    """
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# ---- Test Cases ----
if __name__ == "__main__":
    print(merge_sort([38, 27, 43, 3, 9, 82, 10]))  # Expected: [3, 9, 10, 27, 38, 43, 82]
    print(merge_sort([5, 1, 4, 2, 8]))              # Expected: [1, 2, 4, 5, 8]
    print(merge_sort([1, 2, 3, 4, 5]))              # Expected: [1, 2, 3, 4, 5]
    print(merge_sort([5, 4, 3, 2, 1]))              # Expected: [1, 2, 3, 4, 5]
    print(merge_sort([]))                            # Expected: []
    print(merge_sort([1]))                           # Expected: [1]
    print(merge_sort([3, 3, 3, 3]))                  # Expected: [3, 3, 3, 3]
