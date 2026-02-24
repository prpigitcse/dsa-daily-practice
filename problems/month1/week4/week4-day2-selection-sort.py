"""
Pattern:
Sorting

Problem Statement:
Given an unsorted array of integers, sort it in ascending order using Selection Sort. Modify the array in-place ($O(1)$ extra space). Input: [64, 25, 12, 22, 11] → Output: [11, 12, 22, 25, 64]. Do not use built-in sort functions.

Intuition:
Selection Sort divides the array into a sorted portion (left) and an unsorted portion (right). In each iteration, find the minimum of the unsorted portion and swap it to the front. After $N$ passes, one more element is permanently placed — the key idea is "select the minimum and place it correctly."

Approach:
1. Iterate through the array from index $i = 0$ to $N-1$.
2. Assume `arr[i]` is the minimum. Scan the remaining unsorted portion ($i+1$ to $N-1$) to find the true minimum index.
3. Swap `arr[i]` with `arr[min_index]`.
4. Repeat until the entire array is sorted.

Time Complexity:
$O(N^2)$ in best, average, and worst cases — always scans the remaining unsorted elements, even if already sorted

Space Complexity:
$O(1)$ — in-place, only a few extra variables

Common Mistakes:
- Swapping inside the inner loop instead of **after** finding the minimum
- Forgetting to reset `min_index` for every outer loop iteration
- Assuming it becomes faster for already sorted arrays (it does not — always $O(N^2)$)
- Confusing with Bubble Sort (Selection Sort minimizes swaps; Bubble Sort minimizes passes when optimized)

Code Explanation:
- `def selection_sort(arr)`: Sorts the array in-place and returns it.
- `for i in range(len(arr))`: Outer loop: `i` marks the boundary between the sorted left portion and unsorted right portion.
- `smallest = arr[i]`: Assume the first element of the unsorted portion is the minimum.
- `min_index = i`: Track the index of the current minimum.
- `for j in range(i+1, len(arr))`: Scan the rest of the unsorted portion.
- `if arr[j] < smallest: smallest = arr[j]; min_index = j`: Update the minimum if a smaller element is found.
- `arr[i], arr[min_index] = arr[min_index], arr[i]`: **Swap after the inner loop completes** (not inside it). Places the true minimum at position `i`. Python's simultaneous assignment avoids needing a temp variable.
- `return arr`: The same array object, sorted in-place.

Final Thoughts:
Selection Sort performs at most $N$ swaps, useful when write operations are costly. However, it always runs in $O(N^2)$ regardless of input. Its value lies in understanding loop invariants and sorting logic before moving to $O(N \log N)$ algorithms like Merge Sort or Quick Sort.
"""

# The Problem: Sort an Array (Selection Sort)
# Given an unsorted array of integers, sort it in ascending order using the Selection Sort algorithm.
# Input: [64, 25, 12, 22, 11]
# Output: [11, 12, 22, 25, 64]
# Constraint: You must strictly use the Selection Sort logic.

def selection_sort(arr):
    for i in range(len(arr)):
        smallest = arr[i]
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < smallest:
                smallest = arr[j]
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
        
    return arr

print(selection_sort([64, 25, 12, 22, 11]))
print(selection_sort([1, 2, 3, 4, 5]))
print(selection_sort([5, 4, 3, 2, 1]))
print(selection_sort([1, 5, 2, 4, 3]))
print(selection_sort([1, 1, 1, 1, 1]))
print(selection_sort([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]))
print(selection_sort([1, 2, 1, 2, 3, 5, 4, 4, 3, 2, 1]))