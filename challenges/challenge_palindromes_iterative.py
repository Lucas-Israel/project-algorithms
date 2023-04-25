def is_palindrome_iterative(word):
    if len(word) == 0:
        return False
    finish = len(word)
    to_return = True
    for index, _ in enumerate(range(0, finish)):
        if word[index] != word[finish - (1 + index)]:
            to_return = False

    return to_return
