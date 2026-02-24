"""
Pattern:
Sorting

Problem Statement:
Given an unsorted array of integers, sort it in ascending order using the Insertion Sort algorithm. Modify the array in-place ($O(1)$ extra space). 
Input: [12, 11, 13, 5, 6] → Output: [5, 6, 11, 12, 13]. 
Constraint: You must strictly use the Insertion Sort logic. Do not use built-in sort functions.

Intuition:
Think of sorting a hand of playing cards. You keep the sorted cards in your left hand and pick up one unsorted card at a time. You scan your sorted hand from right to left, shift the larger cards over to make room, and insert the new card into its correct position. The left side of the array is progressively built up as a fully sorted section.

Approach:
1. Iterate from index $i = 1$ to $N-1$ (assume the first element at index 0 is already sorted).
2. Store the current element in a variable called `item` (this is the card you just picked up).
3. Use an inner loop pointer $j$ starting at $i - 1$ to scan the sorted left portion backwards.
4. While $j \ge 0$ and the element `arr[j]` is strictly greater than `item`, shift the element one position to the right (`arr[j + 1] = arr[j]`).
5. Once the loop stops, insert the `item` into the vacated spot (`arr[j + 1] = item`).

Time Complexity:
- Worst & Average Case: $O(N^2)$ — Occurs when the array is reverse sorted, requiring every element to be shifted to the very beginning.
- Best Case: $O(N)$ — Occurs when the array is already sorted. The inner `while` loop immediately fails, so no shifting happens.

Space Complexity:
$O(1)$ — Insertion Sort is an in-place algorithm requiring only a few variables (`item`, `i`, `j`).

Common Mistakes:
- Forgetting the boundary check `j >= 0` in the `while` loop, which will cause an `IndexError` when scanning past the front of the array.
- Overwriting values instead of shifting them (forgetting to store `arr[i]` in the temporary `item` variable first).
- Using `arr[j] >= item` instead of `arr[j] > item`. Using `>=` causes the algorithm to swap identical elements, which breaks the "stability" of the sort.

Code Explanation:
- `def insertion_sort(arr)`: Sorts the array in-place.
- `for i in range(1, len(arr))`: Start at the second element, treating the first element as a sorted sub-array of length 1.
- `item = arr[i]`: The value we are currently trying to place.
- `j = i - 1`: The index of the last element in the sorted portion.
- `while j >= 0 and arr[j] > item`: Look backwards. As long as we haven't fallen off the left edge, and the current sorted element is bigger than our item...
- `arr[j + 1] = arr[j]`: ...shift the larger element one spot to the right to make room.
- `j -= 1`: Move the pointer left to check the next element.
- `arr[j + 1] = item`: Once we find a smaller element (or hit the start of the array), drop the `item` into the correct slot.
- `return arr`: Return the fully sorted array.

Final Thoughts:
Insertion Sort is highly efficient for small datasets or arrays that are already partially sorted (it is an "adaptive" algorithm). It is also a "stable" sort, meaning duplicate elements retain their original relative order. While it shares the same $O(N^2)$ worst-case time complexity as Bubble and Selection sort, its $O(N)$ best-case makes it the fastest of the three in real-world, nearly-sorted scenarios.
"""

# The Problem: Sort an Array (Insertion Sort)
# Given an unsorted array of integers, sort it in ascending order using the Insertion Sort algorithm. Modify the array in-place O(1) space.
# Input: [12, 11, 13, 5, 6] Output: [5, 6, 11, 12, 13]
# Constraint: You must strictly use the Insertion Sort logic.

def insertion_sort(arr):
    for i in range(1, len(arr)):
        item = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = item

    return arr

print(insertion_sort([12, 11, 13, 5, 6]))
print(insertion_sort([64, 25, 12, 22, 11]))
print(insertion_sort([1, 2, 3, 4, 5]))
print(insertion_sort([5, 4, 3, 2, 1]))
print(insertion_sort([1, 5, 2, 4, 3]))
print(insertion_sort([1, 1, 1, 1, 1]))
print(insertion_sort([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]))
print(insertion_sort([1, 2, 1, 2, 3, 5, 4, 4, 3, 2, 1]))
print(insertion_sort([]))