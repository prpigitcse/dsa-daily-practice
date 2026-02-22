"""
Problem Statement:
Given an unsorted array of integers, sort it in ascending order using Selection Sort. Modify the array in-place (O(1) extra space). 
Input: [64, 25, 12, 22, 11] → Output: [11, 12, 22, 25, 64]. 
Do not use built-in sort functions. Implement the standard iterative Selection Sort algorithm.

Intuition:
Selection Sort works by dividing the array into two parts: a sorted portion on the left and an unsorted portion on the right. 
In each iteration, we assume the first element of the unsorted portion is the smallest, then scan the remaining elements to find the actual smallest element. 
We then swap it with the first unsorted element. After every pass, one more element is permanently placed in its correct position. 
The key idea is “select the minimum and place it correctly.”

Approach:
1. Iterate through the array from index i = 0 to n-1.
2. Assume arr[i] is the minimum element.
3. Traverse the remaining unsorted portion (i+1 to n-1) to find the true minimum.
4. Track the index of the smallest element found.
5. Swap arr[i] with arr[min_index].
6. Repeat until the entire array is sorted.

Time Complexity:
O(N^2) in best, average, and worst cases — because we always scan the remaining unsorted elements fully, even if the array is already sorted.

Space Complexity:
O(1) — Selection Sort is in-place and uses only a few extra variables.

Common Mistakes:
- Swapping inside the inner loop instead of after finding the minimum.
- Forgetting to reset min_index for every outer loop iteration.
- Assuming it becomes faster for already sorted arrays (it does not).
- Confusing it with Bubble Sort (Selection Sort minimizes swaps; Bubble Sort minimizes passes when optimized).
- Using it for large datasets in production (it is inefficient for large N).

Final Thoughts:
Selection Sort is simple, predictable, and performs at most N swaps, which can be useful when write operations are costly. 
However, it always runs in O(N^2) time, making it impractical for large datasets. 
Its real value lies in building a strong understanding of sorting logic, loop invariants, and algorithm structure — foundational skills before moving to more efficient algorithms like Merge Sort or Quick Sort.
"""
# The Problem: Sort an Array (Selection Sort)
# Given an unsorted array of integers, sort it in ascending order using the Selection Sort algorithm. Modify the array in-place (O(1) space).
# Input: [64, 25, 12, 22, 11]
# Output: [11, 12, 22, 25, 64]
# Constraint: You must strictly use the Selection Sort logic.

def selection_sort(arr):
    for i in range(len(arr)):
        smallest = arr[i]
        index = i
        for j in range(i+1, len(arr)):
            if arr[j] < smallest:
                smallest = arr[j]
                index = j

        arr[i], arr[index] = smallest, arr[i]
        
    return arr

print(selection_sort([64, 25, 12, 22, 11]))
print(selection_sort([1, 2, 3, 4, 5]))
print(selection_sort([5, 4, 3, 2, 1]))
print(selection_sort([1, 5, 2, 4, 3]))
print(selection_sort([1, 1, 1, 1, 1]))
print(selection_sort([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]))
print(selection_sort([1, 2, 1, 2, 3, 5, 4, 4, 3, 2, 1]))