def find_max(numbers):
    largest_num = numbers[0]
    for x in numbers:
        if largest_num < x:
            largest_num = x
    return largest_num


print(find_max([1, 2, 3, 4]))

# using while loop


def find_max2(numbers):
    largest_num = numbers[0]
    for x in numbers:
        while largest_num < x:
            largest_num = x
    return largest_num


print(find_max2([1, 2, 3, 4, 5, 676]))