"""
Pattern:
Binary Search

Problem Statement:
A peak element is an element that is strictly greater than its neighbors. Given a 0-indexed integer array `nums`, find a peak element and return its index. If the array contains multiple peaks, return the index to any of the peaks. You may imagine that `nums[-1] = -∞` and `nums[n] = -∞`.
Input: `nums = [1, 2, 1, 3, 5, 6, 4]` -> Output: `1` or `5`.
Constraint: You must write an algorithm that runs in $O(\log N)$ time.

Intuition:
We can find a peak by treating the array as a mountain range and following the upward slope. If we drop onto a random point `mid` and see that the next step `mid + 1` is higher, we are walking uphill, meaning there *must* be a peak to our right. Conversely, if `mid + 1` is lower, we are on a downward slope, meaning there *must* be a peak to our left (or `mid` itself is the peak). By always moving towards the higher ground, we can eliminate half the mountain at every step using Binary Search, even though the array is not globally sorted.

Approach:
1. Initialize two pointers: `left = 0` and `right = len(nums) - 1`.
2. Run a `while` loop as long as `left < right`.
3. Calculate the `mid` point.
4. Compare `arr[mid]` to its right neighbor `arr[mid + 1]`.
5. If `arr[mid] < arr[mid + 1]` (ascending slope), the peak is to the right. Set `left = mid + 1`.
6. If `arr[mid] > arr[mid + 1]` (descending slope), the peak is at `mid` or to its left. Set `right = mid`.
7. When the loop terminates (`left == right`), the pointers will have converged on a peak. Return `left`.

Time Complexity:
$O(\log N)$ — We divide the search space in half during every iteration, vastly outperforming a linear $O(N)$ scan.

Space Complexity:
$O(1)$ — We only use a few integer variables (`left`, `right`, `mid`) to track our position.

Common Mistakes:
- Using `left <= right` in the `while` loop condition. Because we are accessing `arr[mid + 1]`, a `<=` condition can cause an `IndexError` when `left` and `right` converge on the last element.
- Setting `right = mid - 1` when `arr[mid] > arr[mid + 1]`. If `mid` is the peak, subtracting 1 will skip over it. `right` must be set to `mid` to keep the potential peak inside the search space.
- Overcomplicating the logic by checking both `arr[mid - 1]` and `arr[mid + 1]`. You only need to check one direction to determine the slope!

Code Explanation:
- `def peak_element_index(arr)`: The main function to find a peak index.
- `left = 0; right = len(arr) - 1`: Initializes the search boundaries to the full array.
- `while left < right`: Loops until the two pointers meet.
- `mid = (left + right) // 2`: Finds the middle index.
- `if arr[mid] < arr[mid + 1]`: Checks if the slope is rising to the right.
- `left = mid + 1`: If rising, the peak must be further right.
- `else:`: Implies `arr[mid] > arr[mid + 1]` (the slope is falling).
- `right = mid`: If falling, the peak is `mid` itself or somewhere to the left.
- `return left`: Once `left` equals `right`, we have found a peak. Return its index.

Final Thoughts:
This problem shatters the common misconception that Binary Search only works on fully sorted arrays. The true requirement for Binary Search is simply that we have a reliable way to eliminate half of the search space at each step. By leveraging local gradients (slopes), we can apply $O(\log N)$ efficiency to seemingly chaotic data.
"""
# The Problem: Find Peak Element
# A peak element is an element that is strictly greater than its neighbors.Given a 0-indexed integer array nums, find a peak element and return its index. If the array contains multiple peaks, return the index to any of the peaks.You may imagine that the elements outside the array are negative infinity (nums[-1] = -\infty and nums[n] = -\infty). This means an element at the very edge is a peak if it is greater than its single neighbor.
# Input: nums = [1, 2, 3, 1] Output: 2 (Index of value 3. It is greater than 2 and 1.)
# Input: nums = [1, 2, 1, 3, 5, 6, 4] Output: 1 or 5 (Index 1 is the peak value 2. Index 5 is the peak value 6. Returning either is correct.)
# Constraint: You must write an algorithm that runs in O(log N) time. (A simple O(N) loop scanning for nums[i] > nums[i+1] is not allowed).


def peak_element_index(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left

print(peak_element_index([1, 2, 3, 1]))
print(peak_element_index([1, 2, 1, 3, 5, 6, 4]))