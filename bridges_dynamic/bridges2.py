from contextlib import contextmanager
from time import time


@contextmanager
def timing():
    start = time()
    yield
    end = time()
    print("Took {}s".format(end - start))

class BridgeSolver(object):

    def __init__(self, bridges):
        length = len(bridges)
        self.bridges = bridges
        self.bridgesLen = length
        self.crosses = [[None for x in range(length)] for y in range(length)]

    def maxToll(self):
        validLayouts = self.findValidLayouts()

        mToll = 0
        mLayout = None
        for bridgeLayout in validLayouts:
            toll = 0
            for i in bridgeLayout:
                toll += self.bridges[int(i)][2]
            if mToll < toll:
                mToll = toll;
                mLayout = bridgeLayout
        return (mToll, mLayout)

    def findValidLayouts(self):
        layouts = []
        for row in range(self.bridgesLen):
            # print("Proc row: {}".format(row))

            # for col in range(row + 1, self.bridgesLen):
                # print("\tProc col: {}".format(col))
            newLayouts = self.findValidLayoutsFrom([row], row, row + 1)
            layouts += newLayouts
        # for r in self.crosses:
        #     print("| ", end='')
        #     for c in r:
        #         print("{} ".format(" " if c is True or c is None else "F"), end='')
        #     print("|")
        # print("Layouts: {}".format(layouts))
        return layouts

    def findValidLayoutsFrom(self, layout, row, col):
        if col >= self.bridgesLen:
            return [layout]
        if self.doCross(row, col):
            return self.findValidLayoutsFrom(layout, row, col + 1)

        # print("Current layout: {}".format(layout))
        for b in range(1, len(layout)):
            # print("Checking {}, {}".format(layout[b], col))
            if self.doCross(layout[b], col):
                # print("They cross")
                return self.findValidLayoutsFrom(layout, row, col + 1)

        return self.findValidLayoutsFrom(layout, row, col + 1) + self.findValidLayoutsFrom(layout + [col], row, col + 1)


    def doCross(self, b1, b2):
        cross = self.crosses[b1][b2]
        if cross is not None:
            return cross

        w = self.bridges[b1]
        e = self.bridges[b2]
        cross = False

        if (w[0] <= e[0] and w[1] >= e[1]) or (w[0] >= e[0] and w[1] <= e[1]):
            cross = True

        self.crosses[b1][b2] = cross
        self.crosses[b2][b1] = cross
        return cross


def build(bridges):
    solver = BridgeSolver(bridges)
    (toll, layout) = solver.maxToll()
    return toll



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

    # with timing():
    #     print("Found: {}".format(build(input1)))
    # with timing():
    #     print("Found: {}".format(build(input2)))
    # with timing():
    #     print("Found: {}".format(build(input3)))
    # with timing():
    #     print("Found: {}".format(build(input4)))
    with timing():
        print("Found: {} should be {}".format(build(input5), 3*60))
    with timing():
        print("Found: {} should be {}".format(build(input6), 14))
