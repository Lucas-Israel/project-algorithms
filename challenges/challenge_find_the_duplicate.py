class CustomError(Exception):
    pass


class Found_Duplicate(Exception):
    pass


def merge_sort(numbers, start=0, end=None):
    if not isinstance(numbers[0], int) or numbers[0] < 0:
        raise CustomError
    if end is None:
        end = len(numbers)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(numbers, start, mid)
        merge_sort(numbers, mid, end)
        merge(numbers, start, mid, end)


def merge(numbers, start, mid, end):
    left = numbers[start:mid]
    right = numbers[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            numbers[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            numbers[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            numbers[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            numbers[general_index] = right[right_index]
            right_index = right_index + 1


def len_check(nums):
    if len(nums) <= 1:
        raise CustomError


def duplicate_checker(nums):
    for i, ele in enumerate(nums):
        if i == 0:
            pass
        if nums[i - 1] == ele:
            return ele
    return False


def find_duplicate(nums):
    try:
        len_check(nums)
        merge_sort(nums)

    except CustomError:
        return False

    return duplicate_checker(nums)


if __name__ == "__main__":
    n_list = [[3, 1, 5, 5], [1, 2, 3], [1, 2, 3, 4, 3]]
    for n in n_list:
        a = find_duplicate(n)
        print(a)
