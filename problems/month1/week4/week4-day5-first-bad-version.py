"""
Pattern:
Binary Search

Problem Statement:
You are given $N$ versions of a software product `[1, 2, ..., N]`. If a version is bad, all subsequent versions are also bad. You have a helper function `is_bad_version(version)` that returns `True` if a version is bad and `False` if it is good. Write a function to find the first bad version while minimizing the number of API calls.
Constraint: You must achieve $O(\log N)$ time complexity.

Intuition:
Since the versions go from all "good" to all "bad" at a specific point, the results of `is_bad_version` look like a sorted boolean array (e.g., `[False, False, True, True, True]`). Because this sequence is strictly ordered, we can apply Binary Search to find the exact boundary where `False` turns to `True`, effectively cutting the search space in half with every check.

Approach:
1. Initialize two pointers: `first_version = 1` and `last_version = n` to represent the search space.
2. Run a `while` loop as long as `first_version < last_version`.
3. Calculate the `mid` point. 
4. Call the API: `is_bad_version(mid)`.
5. If it returns `True`, the first bad version is either this `mid` version or something before it. Narrow the search to the left half by setting `last_version = mid`.
6. If it returns `False`, the current version is good, meaning the first bad version *must* be strictly after it. Narrow the search to the right half by setting `first_version = mid + 1`.
7. When the two pointers meet, they will land exactly on the first bad version.

Time Complexity:
$O(\log N)$ — We divide the search space in half during every iteration, vastly outperforming a linear $O(N)$ scan. 

Space Complexity:
$O(1)$ — We only use a few integer variables (`first_version`, `last_version`, `mid`) to track our position.

Common Mistakes:
- Setting `last_version = mid - 1` when `is_bad_version(mid)` is `True`. If `mid` happens to be the very first bad version, subtracting 1 completely removes the correct answer from the search space.
- Using a standard Binary Search `while first_version <= last_version` condition, which can easily lead to an infinite loop when shifting boundaries without `+1` or `-1`. Using `<` guarantees termination when they meet.
- Integer overflow in other languages: While Python handles arbitrarily large integers, in languages like Java or C++, `(left + right) / 2` can cause an overflow error. The safer formula is `left + (right - left) / 2`.

Code Explanation:
- `def first_bad_version(n)`: The main function accepting the total number of versions.
- `if not is_bad_version(n): return None`: An early exit check. If the latest version is good, there are no bad versions.
- `first_version = 0; last_version = n`: Initializes the search boundaries.
- `while first_version < last_version`: The loop continues until the pointers converge on a single version.
- `mid = (first_version + last_version) // 2`: Finds the middle index.
- `if is_bad_version(mid): last_version = mid`: If bad, the boundary is at `mid` or to its left.
- `else: first_version = mid + 1`: If good, the boundary is strictly to the right.
- `return first_version`: Returns the converged pointer, which is the index of the first bad version.

Final Thoughts:
This pattern is known as "Binary Search for a Boundary" or "Binary Search on an Answer." It is incredibly versatile and appears constantly in systems engineering, such as finding the exact commit where a bug was introduced (which is exactly how the `git bisect` command works under the hood).
"""
# The Problem: First Bad Version
# You are a product manager leading a team to develop a new software product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.Suppose you have $N$ versions [1, 2, ..., N] and you want to find out the first bad one, which causes all the following ones to be bad.You are given a helper API function is_bad_version(version) which returns a boolean:True if the version is bad.False if the version is good.
# Write a function first_bad_version(n) to find the first bad version. You must minimize the number of calls to the API.Input: n = 5, and version 4 is the first bad version.
# Output: 4
# is_bad_version(3) -> False
# is_bad_version(5) -> True
# is_bad_version(4) -> True
# Constraint: You must achieve O(log N) time complexity. You cannot just run a for loop from 1 to N checking every version.

def is_bad_version(version):
    # Mock API for testing
    first_bad = 7 # Change this to test different scenarios
    return version >= first_bad

def first_bad_version(n):
    if not is_bad_version(n):
        return None

    first_version = 0
    last_version = n

    while first_version < last_version:
        mid = (first_version + last_version) // 2
        if is_bad_version(mid):
            last_version = mid
        else:
            first_version = mid + 1

    return first_version

print(first_bad_version(10))
