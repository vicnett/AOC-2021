# Day 1
def depth_increases(some_int_list):
    return [
            value > some_int_list[max(n - 1, 0)]
            for n, value in enumerate(some_int_list)
            ]

def sliding_list(some_list, size):
    return [
            sum(some_list[i:i+size])
            for i in range(0, len(some_list) - (size - 1))
            ]

# Day 2
def record_position(hpos, depth, itinerary = []):
    itinerary.append([hpos, depth])
    return itinerary

def follow_course_without_aim(directions):
    hpos = 0
    depth = 0
    itinerary = record_position(hpos, depth)

    for i in range(0, len(directions)):
        instruction = directions[i][0]
        value = int(directions[i][1])
        if instruction == 'forward':
                hpos += value
        if instruction == 'down':
                depth += value
        if instruction == 'up':
                depth -= value
        itinerary = record_position(hpos, depth, itinerary)

    return itinerary

def follow_course(directions):
    hpos = 0
    depth = 0
    aim = 0
    itinerary = record_position(hpos, depth)

    for i in range(0, len(directions)):
        instruction = directions[i][0]
        value = int(directions[i][1])
        if instruction == 'forward':
                hpos += value
                depth += value * aim
        if instruction == 'down':
                aim += value
        if instruction == 'up':
                aim -= value
        itinerary = record_position(hpos, depth, itinerary)

    return itinerary

