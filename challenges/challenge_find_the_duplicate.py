class CustomError(Exception):
    pass


def counting_sort_list(highest_number):
    return [0 for _ in range(0, highest_number + 1)]


def len_check(nums):
    if len(nums) <= 1:
        raise CustomError


def number_in_list_check(nums):
    for number in nums:
        if not isinstance(number, int) or number < 0:
            raise CustomError


def duplicate_check(new_list):
    for number in new_list:
        if number > 1:
            return
    raise CustomError


def find_duplicate(nums):
    try:
        len_check(nums)
        number_in_list_check(nums)
        highest_number = max(nums)
        new_list = counting_sort_list(highest_number)

        for number in nums:
            new_list[number] += 1

        duplicate_check(new_list)

    except CustomError:
        return False

    return new_list.index(max(new_list))
