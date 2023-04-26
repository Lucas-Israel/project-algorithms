def merge_sort(string):
    if len(string) <= 1:
        return string
    mid = len(string) // 2
    left = merge_sort(string[:mid])
    right = merge_sort(string[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


# https://www.geeksforgeeks.org/python-program-to-sort-a-string/
#


def is_anagram(first_string: str, second_string: str):
    str1 = "".join(merge_sort(first_string.lower()))
    str2 = "".join(merge_sort(second_string.lower()))

    if len(str1) == 0 or len(str2) == 0:
        return str1, str2, False

    return str1, str2, str1 == str2
