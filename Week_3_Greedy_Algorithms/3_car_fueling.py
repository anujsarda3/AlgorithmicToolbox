# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    n = len(stops)
    stops.insert(0,0)
    stops.append(d)
    curr_stop = 0
    num_fill = 0
    while curr_stop <= n:
        last_stop = curr_stop
        while curr_stop <= n and stops[curr_stop+1]-stops[last_stop] <= m:
            curr_stop += 1
        if curr_stop == last_stop:
            return -1
        if curr_stop <= n:
            num_fill += 1

    return num_fill




if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
