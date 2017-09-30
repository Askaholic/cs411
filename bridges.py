

def build(w, e, bridges, builtBridges=[], level=0):
    # print(("\t"* level) + " {}".format(bridges))
    # print(("\t"* level) + "#{}".format(builtBridges))
    if bridges == []:
        return 0
    else:
        sum1 = -1
        sum2 = -1
        if islegal(bridges[0], builtBridges):
            bridgeVal = bridges[0][2]
            sum1 = build(w, e, bridges[1:], builtBridges + [bridges[0]], level + 1) + bridgeVal
        sum2 = build(w, e, bridges[1:], builtBridges, level + 1)
        return max(sum1, sum2)


def islegal(w, builtBridges):
    for e in builtBridges:
        if (w[0] <= e[0] and w[1] >= e[1]) or (w[0] >= e[0] and w[1] <= e[1]):
            return False
    return True


if __name__ == "__main__":
    print("Example 1")
    bridges = [
        (0, 1, 3),
        (1, 1, 5),
        (1, 2, 4),
        (2, 0, 8)
    ]
    print(build(0, 0, bridges))


    print("Example 2")
    bridges = [
        (0, 1, 3),
        (1, 1, 5),
        (1, 2, 4),
        (2, 0, 8),
        (2, 2, 6)
    ]
    print(build(0, 0, bridges))

    print("Test 1")
    bridges = [
        (0, 0, 4),
        (1, 0, 4),
        (2, 0, 4),
        (2, 2, 4),
        (1, 1, 4)
    ]
    built = []
    print(build(0, 0, bridges, built))
