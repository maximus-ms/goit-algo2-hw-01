import random

## Task 1. Find the maximum and minimum elements in an array
def find_max_min(arr):
    """
    Find the maximum and minimum elements in an array.

    Divide the array into two halves and find the max and min elements
    in each half. Then find the overall max and min elements from the
    elements found in the two halves.

    Parameters
    ----------
    arr : list
        The list of elements to find the maximum and minimum of.

    Returns
    -------
    tuple
        A tuple of two elements, the maximum and minimum elements in the array.
    """
    try:
        l = len(arr)
        if l <= 2: return (arr[0], arr[-1]) if arr[0] < arr[-1] else (arr[-1], arr[0])
    except:
        print("Error! Expected a non-empty list or tuple as input")
        return (None, None)

    # Divide the array into two halves
    left = find_max_min(arr[:l // 2])
    right = find_max_min(arr[l // 2:])

    # Find the overall max and min elements from the elements found in the two halves
    return (min(left[0], right[0]), max(left[1], right[1]))


## Task 2. Find the nth smallest element in an array
def find_nth_smallest(arr, n):
    """
    Find the nth smallest element in an array.

    Parameters
    ----------
    arr : list
        The list of elements to find the nth smallest element of.
    n : int
        The position of the element to find.

    Returns
    -------
    int
        The nth smallest element in the array.
    """
    try:
        l = len(arr)
        if l <= 2: return arr[n] if n < l else None
    except:
        print("Error! Expected a non-empty list or tuple as input")
        return None

    pivot = arr[random.randint(0, l - 1)]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    if n < len(left):
        return find_nth_smallest(left, n)
    elif n < len(left) + len(middle):
        return middle[0]
    else:
        return find_nth_smallest(right, n - len(left) - len(middle))


if __name__ == "__main__":
    print("\nTask 1. Find the maximum and minimum elements in an array")
    arr = [random.randint(-100, 100) for _ in range(16)]
    print(arr)
    min_element, max_element = find_max_min(arr)
    print(f"Minimum element: {min_element}")
    print(f"Maximum element: {max_element}")

    print("\nTask 2. Find the nth smallest element in an array")
    arr = [random.randint(-100, 100) for _ in range(16)]
    print(arr)
    n = random.randint(0, len(arr) - 1)
    nth_element = find_nth_smallest(arr, n)
    print(f"{n}-th smallest element: {nth_element}")

