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
