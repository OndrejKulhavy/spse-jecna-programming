import random
from itertools import islice, permutations


def boat_heuristic(*seats):
    state = list([*seats])
    all_states = generate_perms_heuristics(state)
    return get_best_option(all_states)


def generate_perms_heuristics(state: list):
    if len(state) % 2 == 0:
        end = int(factorial(len(state)) / len(state))
        step = factorial(int(len(state) / 2))
        states = [val for val in perm_with_step(state, end, step)]
    else:
        end = int(factorial(len(state)) / 2)
        step = 2
        if len(state) == 3:
            step = 1
        states = [val for val in perm_with_step_half(state, end, step)]
    return states

def factorial(n):
    if n < 0 or type(n) is not int:
        raise ValueError('Invalid data')
    if n == 0:
        return 1
    return n * factorial(n - 1)

def perm_with_step(state, end, step):
    for perm in islice(permutations(state), 0, end, step):
        yield list(perm)

def perm_with_step_half(state, end, step):
    for perm in islice(permutations(state), 0, end, step):
        yield list(perm)

def get_best_option(states: list):

    evaluated = [evaluate_boat(state) for state in states]
    best_options = find_best_values(states, evaluated)
    return best_options

def evaluate_boat(state: list):

    side_length = int(len(state) / 2)

    left_values = sum(state[:side_length])
    right_values = sum(state[-side_length:])

    return left_values - right_values

def find_best_values(states: list, points: list):

    min_abs = min(abs(num) for num in points)
    best_points = [i for i, num in enumerate(points) if abs(num) == min_abs]

    return [states[val] for val in best_points]