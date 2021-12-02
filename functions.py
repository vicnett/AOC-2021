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

