# Problem: Bubble Sort
# Difficulty: Easy
# Approach: Comparison-based sorting with adjacent swaps
# Time Complexity: O(n^2) worst/average, O(n) best (already sorted)
# Space Complexity: O(1) — in-place sorting
#
# Problem Statement:
# Sort an array of integers in ascending order using the bubble sort
# algorithm. Optimize with early termination if no swaps occur in a pass.

def bubble_sort(arr):
    """
    Sorts the array in-place using bubble sort.
    Optimized: stops early if no swaps occur during a full pass,
    indicating the array is already sorted.

    Args:
        arr: List of comparable elements to sort.

    Returns:
        The sorted list (sorted in-place).
    """
    n = len(arr)

    for i in range(n):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # Early termination: no swaps means array is sorted
        if not swapped:
            break

    return arr


# ---- Test Cases ----
if __name__ == "__main__":
    print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))  # Expected: [11, 12, 22, 25, 34, 64, 90]
    print(bubble_sort([5, 1, 4, 2, 8]))                # Expected: [1, 2, 4, 5, 8]
    print(bubble_sort([1, 2, 3, 4, 5]))                # Expected: [1, 2, 3, 4, 5] (best case)
    print(bubble_sort([5, 4, 3, 2, 1]))                # Expected: [1, 2, 3, 4, 5] (worst case)
    print(bubble_sort([]))                              # Expected: []
    print(bubble_sort([1]))                             # Expected: [1]
    print(bubble_sort([2, 2, 2, 2]))                   # Expected: [2, 2, 2, 2]
