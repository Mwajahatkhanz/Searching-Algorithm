def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if _name_ == "_main_":
    # Example array
    arr = [2, 3, 4, 10, 40]
    target = 10

    print("Array:", arr)
    print("Target:", target)

    # Linear Search
    linear_result = linear_search(arr, target)
    if linear_result != -1:
        print(f"Linear Search: Element found at index {linear_result}")
    else:
        print("Linear Search: Element not found.")

    # Binary Search
    binary_result = binary_search(arr, target)
    if binary_result != -1:
        print(f"Binary Search: Element found at index {binary_result}")
    else:
        print("Binary Search: Element not found.")
