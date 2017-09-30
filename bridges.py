

def build(bridges, builtBridges=[], level=0):
    # print(("\t"* level) + " {}".format(bridges))
    # print(("\t"* level) + "#{}".format(builtBridges))
    if bridges == []:
        return 0
    else:
        sum1 = -1
        if islegal(bridges[0], builtBridges):
            bridgeVal = bridges[0][2]
            sum1 = build(bridges[1:], builtBridges + [bridges[0]], level + 1) + bridgeVal
        sum2 = build(bridges[1:], builtBridges, level + 1)
        return max(sum1, sum2)


def islegal(w, builtBridges):
    for e in builtBridges:
        if (w[0] <= e[0] and w[1] >= e[1]) or (w[0] >= e[0] and w[1] <= e[1]):
            return False
    return True
