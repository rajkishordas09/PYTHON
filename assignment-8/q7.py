def A(arr, n, curr_sum, result):
  if n == 0:
    result.append(curr_sum)
    return
  A(arr, n-1, curr_sum, result)  # Exclude the current element
  A(arr, n-1, curr_sum + arr[n-1], result)  # Include the current element

def print_subset_sums(arr):
  n = len(arr)
  result = []
  A(arr, n, 0, result)
  result.sort()  # Sort the sums for consistent output
  print(result)

# Example usage
arr = [2, 3]
print_subset_sums(arr)  # Output: [0, 2, 3, 5]

arr = [2, 4, 5]
print_subset_sums(arr)  # Output: [0, 2, 4, 5, 6, 7, 9, 11]
