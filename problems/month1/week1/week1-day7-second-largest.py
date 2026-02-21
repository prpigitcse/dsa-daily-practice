"""
Problem Statement:
Given an array of integers, find the second largest element. For example, given [10, 5, 20, 8], the output is 10. If all elements are the same (e.g., [10, 10, 10]) or the array has fewer than 2 elements, return -1 or None.

Intuition:
Finding the second largest requires tracking two values simultaneously: the largest and the second largest. As you traverse, each element either becomes the new largest (pushing the old largest down to second), becomes the new second largest, or is irrelevant. This single-pass approach avoids sorting the entire array.

Approach:
1. If the array has fewer than 2 elements, return None.
2. Initialize largest = arr[0] and second_largest = None.
3. Traverse the array starting from index 1.
4. If arr[i] > largest: update second_largest = largest, then largest = arr[i].
5. Else if arr[i] < largest and (second_largest is None or arr[i] > second_largest): update second_largest = arr[i].
6. Skip duplicates of the largest to handle arrays like [10, 10, 5].
7. Return second_largest, or -1 if no valid second largest exists.

Time Complexity:
O(N) — single pass through the array

Space Complexity:
O(1) — only two tracking variables

Common Mistakes:
- Sorting the array first (O(N log N)) when a single O(N) pass suffices
- Not handling duplicates: [20, 20, 10] should return 10, not 20
- Initializing second_largest to a value like 0 or -infinity without considering that all elements might be negative
- Missing the edge case where all elements are identical

Final Thoughts:
This problem teaches you to track multiple states during a single traversal, a pattern that appears frequently in DSA. The key insight is that you don't need to sort — one careful pass with well-maintained variables is enough. This single-pass thinking is essential for optimizing many array problems.
"""

# Question: Given an array of integers, find the second largest element. (e.g., [10, 5, 20, 8] 
# Output: 10
# Explanation & Logic:This is trickier than finding the maximum.The Logic: You need two variables: largest and second_largest.Traversal:If the current number is greater than largest: Update second_largest to be the old largest, then update largest to the new number.If the current number is smaller than largest but bigger than second_largest: Update second_largest only.Edge Case: What if the array is [10, 10, 10]? Does a second largest exist? (Usually, we return -1 or handle duplicates depending on requirements).

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