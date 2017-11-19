from contextlib import contextmanager
from time import time


@contextmanager
def timing():
    start = time()
    yield
    end = time()
    print("Took {}s".format(end - start))


class BridgeSolver(object):

    def __init__(self, bridges, w, e):
        self.bridges = bridges
        self.w = w
        self.e = e
        self.tolls = {}
        self.maxTollSum = 0

        self._initToll()
        # for r in range(w):
        #     print("| ", end='')
        #     for c in range(e):
        #         print("{} ".format(self.tolls.get("{}|{}".format(r, c), " ")), end='')
        #     print("|")

    def _initToll(self):
        self.maxTollSum = 0
        for bridge in self.bridges:
            self.tolls["{}|{}".format(bridge[0], bridge[1])] = bridge[2]

    def maxToll(self):
        self._initToll()
        self._maxToll(0, 0)
        return self.maxTollSum

    def _maxToll(self, w, e):

        for i in range(self.w):
            for j in range(self.e):
                currToll = self.getToll(i, j)
                leftToll = self.getToll(i - 1, j)
                upToll = self.getToll(i, j - 1)
                diagToll = self.getToll(i - 1, j - 1)
                currMax = max(currToll + diagToll, leftToll, upToll)

                if currMax > self.maxTollSum:
                    self.maxTollSum = currMax
                self.setToll(i, j, currMax)

    def getToll(self, w, e):
        return self.tolls.get("{}|{}".format(w, e), 0)

    def setToll(self, w, e, toll):
        self.tolls["{}|{}".format(w, e)] = toll

def build(bridges, w, e):
    solver = BridgeSolver(bridges, w, e)
    return solver.maxToll()

if __name__ == "__main__":
    input1 = [
        [0, 1, 3],
        [1, 0, 6],
        [2, 1, 5],
        [2, 2, 2]
    ]
    input2 = [
        [0, 1, 3],
        [1, 1, 5],
        [1, 2, 4],
        [2, 0, 8]
    ]
    input3 = [
        [0, 1, 3],
        [1, 1, 5],
        [1, 2, 4],
        [2, 0, 8],
        [2, 2, 6]
    ]
    input4 = [
        [0, 0, 4],
        [1, 0, 4],
        [2, 0, 4],
        [2, 1, 4],
        [2, 2, 4]
    ]
    input5 = []
    for i in range(60):
        for j in range(60):
            input5.append([i, j, 3])

    input6 = []
    for  i in range(12):
        input6.append([i, i, 1])
    input6.append([0, 11, 13])
    input6.append([11, 0, 14])

    with timing():
        print("Found: {}".format(build(input1, 3, 3)))
    with timing():
        print("Found: {}".format(build(input2, 3, 3)))
    with timing():
        print("Found: {}".format(build(input3, 3, 3)))
    with timing():
        print("Found: {}".format(build(input4, 3, 3)))
    with timing():
        print("Found: {} should be {}".format(build(input5, 60, 60), 3*60))
    with timing():
        print("Found: {} should be {}".format(build(input6, 12, 12), 14))
