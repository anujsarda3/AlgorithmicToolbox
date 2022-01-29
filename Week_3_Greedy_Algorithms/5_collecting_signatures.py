# python3

from collections import namedtuple
from sys import stdin

Segment = namedtuple('Segment', 'start end')


def compute_optimal_points(segments):
    segments.sort()
    n = len(segments)
    i = 0
    last_end = segments[0].end
    output = []
    while i < n:
        while i < n and segments[i].start <= last_end:
            if last_end > segments[i].end:
                last_end = segments[i].end
            i += 1

        output.append(last_end)
        if i < n:
            last_end = segments[i].end

    return output





if __name__ == '__main__':
    n, *data = map(int, stdin.read().split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    assert n == len(input_segments)
    output_points = compute_optimal_points(input_segments)
    print(len(output_points))
    print(*output_points)

