def is_even_number(number):
    return number % 2 == 0


def do_next_step(number):
    if is_even_number(number):
        return number / 2
    else:
        return number * 3 + 1
