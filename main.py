def is_even_number(number):
    return number % 2 == 0


def do_next_step(number):
    if is_even_number(number):
        return number / 2
    else:
        return number * 3 + 1


def count_steps(number):
    count_of_steps = 0
    while number != 1:
        number = do_next_step(number)
        count_of_steps += 1
    return count_of_steps


def generate_range(start, end):
    result = {}
    for x in range(start, end + 1):
        result[x] = 0
    return result


def get_count_of_steps_for_every_number(start, end):
    result = generate_range(start, end)
    for x in range(start, end + 1):
        result[x] = count_steps(x)
    return result