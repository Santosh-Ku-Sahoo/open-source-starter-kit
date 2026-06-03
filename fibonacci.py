# Problem: Fibonacci Sequence
# Difficulty: Easy
# Approach: Iterative, Memoized Recursive
# Time Complexity: O(n) for both approaches
# Space Complexity: O(1) iterative, O(n) memoized recursive
#
# Problem Statement:
# Compute the nth Fibonacci number (0-indexed: F(0)=0, F(1)=1)
# and generate the full Fibonacci sequence up to n terms.


def fibonacci_iterative(n):
    """
    Return the nth Fibonacci number using iteration.
    Uses constant space by tracking only the last two values.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0:
        return 0
    if n == 1:
        return 1

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr

    return curr


def fibonacci_memoized(n, memo=None):
    """
    Return the nth Fibonacci number using recursion with memoization.
    Avoids redundant calculations by caching previously computed values.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]


def fibonacci_sequence(n):
    """
    Generate a list of the first n Fibonacci numbers.
    Returns an empty list for n <= 0.
    """
    if n <= 0:
        return []

    sequence = [0]
    if n == 1:
        return sequence

    sequence.append(1)
    for i in range(2, n):
        sequence.append(sequence[i - 1] + sequence[i - 2])

    return sequence


# ---- Test Cases ----
if __name__ == "__main__":
    # Test nth Fibonacci number (iterative)
    print("--- Iterative Approach ---")
    nth_tests = [
        (0, 0),
        (1, 1),
        (2, 1),
        (5, 5),
        (10, 55),
        (20, 6765),
    ]

    all_passed = True
    for n, expected in nth_tests:
        result = fibonacci_iterative(n)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  F({n}) = {result}  [{status}]")
    print(f"  All tests passed: {all_passed}\n")

    # Test nth Fibonacci number (memoized)
    print("--- Memoized Recursive Approach ---")
    all_passed = True
    for n, expected in nth_tests:
        result = fibonacci_memoized(n)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  F({n}) = {result}  [{status}]")
    print(f"  All tests passed: {all_passed}\n")

    # Test Fibonacci sequence generation
    print("--- Fibonacci Sequence ---")
    seq_tests = [
        (0, []),
        (1, [0]),
        (2, [0, 1]),
        (5, [0, 1, 1, 2, 3]),
        (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]),
    ]

    all_passed = True
    for n, expected in seq_tests:
        result = fibonacci_sequence(n)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  sequence({n}) = {result}  [{status}]")
    print(f"  All tests passed: {all_passed}\n")
