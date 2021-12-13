from functions import *

input_file = open('day-02.input', 'r')

raw_input = input_file.read().splitlines()

directions = [ n.split() for n in raw_input ]

itinerary = follow_course_without_aim(directions)

print(f'Part one answer: {itinerary[-1][0] * itinerary[-1][1]}')

itinerary = follow_course(directions)

print(f'Part two answer: {itinerary[-1][0] * itinerary[-1][1]}')

