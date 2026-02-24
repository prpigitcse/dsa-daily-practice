"""
Problem Statement:
Given two sorted integer arrays `arr1` and `arr2`, return a new array that contains all elements from both arrays in sorted order.
Input: `arr1 = [1, 3, 5, 7]`, `arr2 = [2, 4, 6, 8]` -> Output: `[1, 2, 3, 4, 5, 6, 7, 8]`.
Constraint: You must achieve $O(N + M)$ time complexity. You cannot simply concatenate the arrays and call `sort()`.

Intuition:
Since both arrays are already sorted, we can think of them like two separate lines of people arranged by height. If we want to merge them into a single sorted line, we just need to compare the person at the front of line A with the person at the front of line B. The shorter person steps into the new line, and the next person in their original line steps up. We repeat this "zipper" motion until one line is empty, and then simply append everyone remaining in the other line.

Approach:
1. Initialize an empty `result` array to store the merged elements.
2. Initialize two pointers, $i = 0$ and $j = 0$, to track the current index in `arr1` and `arr2`, respectively.
3. Use a `while` loop that continues as long as both $i$ and $j$ are within the bounds of their respective arrays.
4. Compare `arr1[i]` and `arr2[j]`. Append the smaller value to `result` and increment the corresponding pointer.
5. Once the loop terminates (meaning one array has been fully traversed), there may be remaining elements in the other array. Since the original arrays are already sorted, we can safely append the entire remaining portion directly to `result`.

Time Complexity:
$O(N + M)$ — We iterate through each element in both arrays exactly once, where $N$ is the length of `arr1` and $M$ is the length of `arr2`.

Space Complexity:
$O(N + M)$ — We create a new `result` array that holds all elements from both input arrays.

Common Mistakes:
- Forgetting to handle the "leftovers" after the main `while` loop finishes. One array will always run out before the other (unless they are exactly identical in length and values).
- Trying to modify one of the arrays in-place instead of returning a new array. While in-place merging is possible, it is significantly more complex and usually requires $O(N \times M)$ time unless advanced techniques are used.
- Using `arr.pop(0)` instead of pointers. `pop(0)` on a Python list is an $O(N)$ operation, which would destroy the $O(N + M)$ time complexity and make the algorithm $O(N^2)$.

Code Explanation:
- `def merge_two_sorted_array(arr1, arr2)`: Function accepts two sorted lists.
- `result = []`: Initializes the output array.
- `i = j = 0`: Sets both pointers to the start of their respective arrays.
- `while i < len(arr1) and j < len(arr2)`: The loop runs until one of the pointers falls off the end of its array.
- `if arr1[i] < arr2[j]`: Compares the current elements.
- `result.append(arr1[i]); i += 1`: If the element in `arr1` is smaller, append it and move the $i$ pointer.
- `else: result.append(arr2[j]); j += 1`: Otherwise, append the element from `arr2` and move the $j$ pointer.
- `result += arr1[i:]`: Appends any remaining elements from `arr1`. If $i$ has already reached the end, this safely appends an empty list without throwing an error.
- `result += arr2[j:]`: Appends any remaining elements from `arr2`.
- `return result`: Returns the final merged list.

Final Thoughts:
This "zipper" technique is the exact logic that powers the "Merge" step of the classic Merge Sort algorithm. Mastering this $O(N + M)$ pointer manipulation is crucial because it proves you can evaluate and combine multiple datasets linearly without resorting to brute-force $O(N^2)$ comparisons or lazy built-in functions.
"""
# The Problem: Merge Two Sorted Arrays
# Given two sorted integer arrays arr1 and arr2, return a new array that contains all elements from both arrays in sorted order.
# Input: arr1 = [1, 3, 5, 7], arr2 = [2, 4, 6, 8] Output: [1, 2, 3, 4, 5, 6, 7, 8]
# Input: arr1 = [1, 2], arr2 = [3, 4, 5] Output: [1, 2, 3, 4, 5]
# Constraint:You must achieve $O(N + M)$ time complexity.You cannot simply concatenate the arrays and call sort() (e.g., return sorted(arr1 + arr2)). That is cheating the algorithm!

def merge_two_sorted_array(arr1, arr2):
    result = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    result += arr1[i:]
    result += arr2[j:]

    return result

print(merge_two_sorted_array([1, 3, 5, 7], [2, 4, 6, 8]))
print(merge_two_sorted_array([1, 2], [3, 4, 5]))
print(merge_two_sorted_array([2, 4], [1, 1, 3]))
print(merge_two_sorted_array([1, 1], [1, 1, 2, 3]))
print(merge_two_sorted_array([3, 6, 7], [2, 5]))