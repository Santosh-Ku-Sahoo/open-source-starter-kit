# Problem: Linear Search
# Difficulty: Easy
# Approach: Sequential scan
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Problem Statement:
# Given an array and a target value, return the index of the target
# if found. Return -1 if the target is not in the array.


def linear_search(arr, target):
    """
    Search for target in arr by checking each element sequentially.
    Returns the index of the first occurrence, or -1 if not found.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def linear_search_all(arr, target):
    """
    Return a list of all indices where target appears in arr.
    Returns an empty list if target is not found.
    """
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices


# ---- Test Cases ----
if __name__ == "__main__":
    # Test first-occurrence search
    print("--- Linear Search (first occurrence) ---")
    tests = [
        ([4, 2, 7, 1, 9], 7, 2),          # found in middle
        ([4, 2, 7, 1, 9], 4, 0),          # found at start
        ([4, 2, 7, 1, 9], 9, 4),          # found at end
        ([4, 2, 7, 1, 9], 5, -1),         # not found
        ([], 1, -1),                        # empty array
        ([3], 3, 0),                        # single element found
        ([3], 5, -1),                       # single element not found
        ([1, 2, 3, 2, 1], 2, 1),           # duplicate — returns first index
        (["a", "b", "c"], "b", 1),         # works with strings
    ]

    all_passed = True
    for arr, target, expected in tests:
        result = linear_search(arr, target)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  search({arr}, {target!r}) = {result}  [{status}]")
    print(f"  All tests passed: {all_passed}\n")

    # Test all-occurrences search
    print("--- Linear Search (all occurrences) ---")
    multi_tests = [
        ([1, 2, 3, 2, 1], 2, [1, 3]),     # multiple matches
        ([1, 2, 3, 4, 5], 6, []),          # no match
        ([7, 7, 7], 7, [0, 1, 2]),         # all match
        ([], 1, []),                        # empty array
        ([5], 5, [0]),                      # single match
    ]

    all_passed = True
    for arr, target, expected in multi_tests:
        result = linear_search_all(arr, target)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  search_all({arr}, {target!r}) = {result}  [{status}]")
    print(f"  All tests passed: {all_passed}\n")
