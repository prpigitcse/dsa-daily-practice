"""
Pattern:
Array

Problem Statement:
Given an array of integers, find the second largest element. For example, given [10, 5, 20, 8], the output is 10. If all elements are the same (e.g., [10, 10, 10]) or the array has fewer than 2 elements, return -1 or None.

Intuition:
Finding the second largest requires tracking two values simultaneously: `largest` and `second_largest`. As you traverse, each element either becomes the new largest (pushing the old largest down to second), becomes the new second largest, or is irrelevant. This single-pass $O(N)$ approach avoids the $O(N \log N)$ cost of sorting.

Approach:
1. If the array has fewer than 2 elements, return None.
2. Initialize `largest = arr[0]` and `second_largest = None`.
3. Traverse from index 1. For each element:
   - If `arr[i] > largest`: set `second_largest = largest`, then `largest = arr[i]`.
   - Else if `arr[i] < largest` and (`second_largest is None` or `arr[i] > second_largest`): update `second_largest`.
4. Skip duplicates of the largest to handle arrays like `[10, 10, 5]`.
5. Return `second_largest`, or -1 if no valid second largest exists.

Time Complexity:
$O(N)$ — single pass through the array

Space Complexity:
$O(1)$ — only two tracking variables

Common Mistakes:
- Sorting the array first — $O(N \log N)$ when a single $O(N)$ pass suffices
- Not handling duplicates: `[20, 20, 10]` should return 10, not 20
- Initializing `second_largest` to 0 or $-\infty$ without considering that all elements might be negative

Code Explanation:
- `if len(arr) < 2: return None`: Guard against arrays too small to have a second element.
- `largest = arr[0]` and `second_largest = None`: Seed the largest with the first element; second largest is unknown.
- `for i in range(1, len(arr))`: Iterate from the second element onward.
- `if arr[i] > largest`: New maximum found: demote old `largest` to `second_largest`, then update `largest`.
- `elif second_largest is not None and arr[i] > second_largest and arr[i] != largest`: The `!= largest` check excludes duplicates of the maximum.
- `elif second_largest is None and arr[i] != largest`: First time we find any element smaller than `largest`, set it as `second_largest`.
- `return second_largest or -1`: If `second_largest` is still None (all duplicates), return -1 as a sentinel.

Final Thoughts:
This problem teaches you to track multiple states during a single traversal. The key insight: you don't need to sort. One careful $O(N)$ pass with well-maintained variables is enough.
"""

# Question: Given an array of integers, find the second largest element.

def second_largest(arr):
    if len(arr) < 2:
        return None
    largest = arr[0]
    second_largest = None
    for i in range(1, len(arr)):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        elif second_largest is not None and arr[i] > second_largest and arr[i] != largest:
            second_largest = arr[i]
        elif second_largest is None and arr[i] != largest:
            second_largest = arr[i]
            
    return second_largest or -1

print(second_largest([10, 5, 20, 8, 20, 10, 10]))