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


def find_the_highest_count_of_steps(actual_range, start):
    result = [0, 0]
    for x in range(start, len(actual_range) + 1):
        if result[0] < actual_range[x]:
            result[0] = actual_range[x]
            result[1] = x
    return str(result[0]) + " " + str(result[1])


def read_line_from_file(path_to_input_file, number_of_line):
    file = open(path_to_input_file)
    line = ""
    for x in range(0, number_of_line):
        line = file.readline()
    return line


def parse_range(line):
    return [int(line[0:line.index(' ')]), int(line[line.index(' ') + 1:])]
