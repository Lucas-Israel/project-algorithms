class CustomError(Exception):
    pass


class Found_Duplicate(Exception):
    pass


def len_check(nums):
    if len(nums) <= 1:
        raise CustomError


def dict_creator(nums):
    new_dict = {}
    for num in nums:
        if not isinstance(num, int) or num < 1:
            raise CustomError
        new_dict[num] = new_dict.get(num, 0) + 1
        if new_dict[num] > 1:
            raise Found_Duplicate(num)
    return new_dict


def find_duplicate(nums):
    try:
        len_check(nums)
        dict_creator(nums)

    except CustomError:
        return False
    except Found_Duplicate as found:
        return found.args[0]

    return False


if __name__ == "__main__":
    n_list = [[3, 1, 5, 5], [1, 2, 3], [1, 2, 3, 4, 3]]
    for n in n_list:
        a = find_duplicate(n)
        print(a)
