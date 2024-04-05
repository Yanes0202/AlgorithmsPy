def binary_search(input_list, item):
    low = 0
    high = len(input_list) - 1

    while low <= high:
        mid = (low + high)
        guess = input_list[mid]
        if guess == item:
            return mid
        if guess > mid:
            high = mid - 1
        else:
            low = mid + 1
    return None


def get_binary_table(size):
    result = []
    for i in range(1, size + 1):
        result.append(i)
    return result
