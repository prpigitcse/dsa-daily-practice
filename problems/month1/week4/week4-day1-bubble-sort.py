"""
Pattern:
Sorting

Problem Statement:
Given an unsorted array of integers, sort it in ascending order using Bubble Sort. Modify the array in-place ($O(1)$ extra space). Input: [5, 1, 4, 2, 8] → Output: [1, 2, 4, 5, 8]. Do not use built-in sort functions. Implement both iterative and recursive versions.

Intuition:
Bubble Sort repeatedly "bubbles" the largest unsorted element to its correct position by comparing adjacent pairs. After each pass, the largest remaining element is in its final position. Subsequent passes can skip the already-sorted suffix, so the comparison count reduces each round.

Approach:
1. **Outer loop:** run from $i = 0$ to $N-1$ ($N$ passes total).
2. **Inner loop:** compare adjacent elements from $j = 1$ to $N - i$ (each pass has one fewer element to check).
3. If `arr[k] > arr[j]`, swap them.
4. After $N$ passes, the array is sorted.
5. **Recursive version:** replace the outer loop with recursion — each call represents one pass, with $i$ incrementing.

Time Complexity:
$O(N^2)$ in worst and average case — $N$ passes, each scanning up to $N$ elements

Space Complexity:
$O(1)$ for iterative version (in-place); $O(N)$ for recursive version (call stack)

Common Mistakes:
- Forgetting to reduce the inner loop range each pass (the last $i$ elements are already sorted)
- Not using a "swapped" flag for early termination — if no swaps occur in a pass, the array is already sorted in $O(N)$
- Using Bubble Sort for large arrays in production — $O(N^2)$ is impractical beyond ~10,000 elements

Code Explanation:

**Iterative `bubble_sort(arr)`:**
- `i = 0`: Outer counter: tracks how many passes have been completed (and thus how many elements are sorted at the tail).
- `while i < len(arr)`: Run `len(arr)` passes total.
- `k = 0; j = 1`: `k` and `j` are adjacent indices (`k` is one behind `j`).
- `while j < len(arr) - i`: Inner loop shrinks by 1 each outer pass because the last `i` elements are already in place.
- `if arr[k] > arr[j]: arr[k], arr[j] = arr[j], arr[k]`: Swap if out of order.
- `k += 1; j += 1`: Advance both adjacent pointers.

**Recursive `bubble_sort_recursion(arr, i, j, k)`:**
- `if i >= len(arr): return arr`: **Outer base case**: all passes done.
- `if j < len(arr) - i`: Still within this pass's inner loop range.
- `return bubble_sort_recursion(arr, i, j+1, k+1)`: Continue inner loop recursively.
- `return bubble_sort_recursion(arr, i + 1)`: Inner loop done; start next pass (j and k reset to default 1 and 0).

Final Thoughts:
Bubble Sort is the simplest sorting algorithm to understand but one of the least efficient. Its value is educational: it introduces sorting through repeated comparisons and swaps. In practice, use Merge Sort ($O(N \log N)$) or Python's built-in Timsort.
"""

# The Problem: Sort an Array (Bubble Sort)
# Given an unsorted array of integers, sort it in ascending order using the Bubble Sort algorithm.
# Input: [5, 1, 4, 2, 8] Output: [1, 2, 4, 5, 8]
# Constraint: You must use the Bubble Sort logic. Do not use built-in sort functions like arr.sort().

def bubble_sort(arr):
    i = 0
    while i < len(arr):
        k = 0
        j = 1
        while j < (len(arr) - i):
            if arr[k] > arr[j]:
                arr[k], arr[j] = arr[j], arr[k]
            k += 1
            j += 1
            
        i += 1

    return arr

def bubble_sort_recursion(arr,i = 0, j = 1, k = 0):
    if i >= len(arr):
        return arr
    
    if j < len(arr) - i:
        if arr[k] > arr[j]:
            arr[k], arr[j] = arr[j], arr[k]
        return bubble_sort_recursion(arr, i, j+1, k+1)

    return bubble_sort_recursion(arr, i + 1)

print(bubble_sort([5, 1, 4, 2, 8]))
print(bubble_sort([]))
print(bubble_sort([5, 1, 5, 1, 8, 8, 3]))
print(bubble_sort([8, 1, 1, 1, 1, 5]))
print(bubble_sort_recursion([5, 1, 4, 2, 8]))
