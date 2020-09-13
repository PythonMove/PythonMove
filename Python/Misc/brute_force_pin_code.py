from time import time
from itertools import product


def pin_code_itertools_int(pin_code):
    pin_code = tuple([int(digit) for digit in pin_code])
    digits = [x for x in range(10)]
    attempts = product(digits, repeat=len(pin_code))
    for attempt in attempts:
        if attempt == pin_code:
            return True
    return False


def pin_code_itertools_str(pin_code):
    pin_code = tuple(pin_code)
    digits = [digit for digit in "0123456789"]
    attempts = product(digits, repeat=len(pin_code))
    for attempt in attempts:
        if attempt == pin_code:
            return True
    return False


def pin_code_int(pin_code):
    last_index = len(pin_code) - 1
    pin_code = [int(x) for x in pin_code.strip()]
    digits = [x for x in range(1, 11)]
    attempt = [0 for _ in range(len(pin_code))]

    while True:
        for digit in digits:
            if attempt == pin_code:
                return True

            attempt[last_index] = digit

        for index in range(last_index, -1, -1):
            if attempt[index] < 9:
                attempt[index] += 1
                break

            attempt[index] = 0


def pin_code_str(pin_code):
    last_index = len(pin_code) - 1
    digits = [char for char in "1234567899"]
    attempt = len(pin_code) * "0"

    while True:
        for digit in digits:
            if attempt == pin_code:
                return True

            attempt = attempt[:last_index] + digit

        nine_count = 0
        index = last_index
        while attempt[index] == "9":
            nine_count += 1
            index -= 1

        attempt = attempt[:index] + chr(ord(attempt[index]) + 1) + (nine_count * digits[0])


def brute_force_pin_code(password, functions):
    print(f"PIN code: {password} -- Length: {len(password)}\n")

    for function in functions:
        print(f"Function: {function.__name__}")
        total_time = 0
        for _ in range(10):
            start_time = time()
            function(password)
            end_time = time() - start_time
            total_time += end_time

        print(f"Average execution time: {round(total_time / 10, 3)}s\n")
    return None


brute_force_pin_code("9999999", [pin_code_str, pin_code_int, pin_code_itertools_str, pin_code_itertools_int])
