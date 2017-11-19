from contextlib import contextmanager
from time import time


@contextmanager
def timing():
    start = time()
    yield
    end = time()
    print("Took {}s".format(end - start))

calls_made = 0

ans = {}

def build(bridges, builtBridges="", level=0):
    global calls_made
    global ans


    if level == len(bridges):
        return 0

    if builtBridges in ans:
        return ans[builtBridges]

    calls_made += 1
    sum1 = -1
    if islegal(bridges[level], bridges, builtBridges):
        bridgeVal = bridges[level][2]
        sum1 = build(bridges, builtBridges + str(level), level + 1) + bridgeVal
    sum2 = build(bridges, builtBridges, level + 1)
    best = max(sum1, sum2)

    ans[builtBridges] = best
    return best


def islegal(w, bridges, builtBridges):
    for i in builtBridges:
        e = bridges[int(i)]
        if (w[0] <= e[0] and w[1] >= e[1]) or (w[0] >= e[0] and w[1] <= e[1]):
            return False
    return True


def build_dynamic(bridges):
    length = len(bridges)
    s = 0
    for i, bridge in enumerate(bridges):
        val = bridge[2]
        crossing_val, crossing = crosses(bridges, length, i)
        # print("Bridge {} crosses {}".format(i, crossing))
        if val > crossing_val:
            s += val
            # print("Taking {} for {}".format(i, val))
            for j in crossing:
                bridges[j] = 0
    return s

def crosses(bridges, length, i):
    s = 0
    l = []
    b = bridges[i]
    for j in range(i + 1, length):
        other = bridges[j]
        if (b[0] <= other[0] and b[1] >= other[1]) or (b[0] >= other[0] and b[1] >= other[1]):
            s += other[2]
            l.append(j)

    return s, l

if __name__ == "__main__":
    input1 = [
        [0, 1, 3],
        [1, 1, 5],
        [1, 2, 4],
        [2, 0, 8],
        [2, 2, 6]
    ]
    input5 = []
    for i in range(0, 4):
        for j in range(0, 4):
            input5.append([i, j, 3])

    input6 = []
    for  i in range(12):
        input6.append([i, i, 1])
    input6.append([0, 11, 13])
    input6.append([11, 0, 14])

    with timing():
        print("Found: {} in {} calls".format(build(input1), calls_made))
    calls = 0
    with timing():
        print("Found: {} in {} calls".format(build(input5), calls_made))
    calls = 0
    with timing():
        print("Found: {} in {} calls".format(build(input6), calls_made))
    # with timing():
    #     print("New way: {}".format(build_dynamic(input1)))
