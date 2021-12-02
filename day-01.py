from functions import *

input_file = open('day-01.input', 'r')

raw_input = input_file.read().splitlines()

int_input = [ int(i) for i in raw_input ]

part_one_answer = sum(depth_increases(int_input))

print(f'part one answer: {part_one_answer}')

part_two_answer = sum(depth_increases(sliding_list(int_input, 3)))

print(f'part two answer: {part_two_answer}')

