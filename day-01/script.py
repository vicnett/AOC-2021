input_file = open('input', 'r')

raw_input = input_file.read().splitlines()

int_input = [ int(i) for i in raw_input ]

def compare(some_int_list):
     return [ value > some_int_list[max(n - 1, 0)] for n, value in enumerate(some_int_list) ]

part_one_answer = sum(compare(int_input))

print(f'part one answer: {part_one_answer}')

sliding_list = [ int_input[i] + int_input[i + 1] + int_input[i + 2] for i in
        range(0, len(int_input)-2) ]

part_two_answer = sum(compare(sliding_list))

print(f'part two answer: {part_two_answer}')


