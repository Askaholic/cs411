# contigsum.py
# Rohan Weeden
# Created: Oct 10, 2017

# Find greatest contiguous sum of a list


def contigsum(seq):
    return contigsum_rec(seq)[0]


def contigsum_rec(seq):
    length = len(seq)

    if length == 1:
        gcs = max(0, seq[0])
        return (gcs, gcs, gcs, seq[0])

    first = contigsum_rec(seq[:(length // 2)])
    second = contigsum_rec(seq[(length // 2):])

    start_gcs = 0
    end_gcs = 0

    if first[1] == first[3]:
        start_gcs = first[1] + second[1]
    else:
        start_gcs = max(first[1], first[3] + second[1])

    if second[2] == second[3]:
        end_gcs = first[2] + second[2]
    else:
        end_gcs = max(second[2], second[3] + first[2])

    return (max(first[0], second[0], first[2] + second[1]), start_gcs, end_gcs, first[3] + second[3])


if __name__ == "__main__":
    print("{} == 17".format(contigsum([6, -8, 4, 3, -1, -2, 5, 8, -9, 4])))
    print("{} == 6".format(contigsum([6])))
    print("{} == 7".format(contigsum([6, 1, -1, -3])))
    print("{} == 58".format(contigsum([5, -2, 1, 12, 10, -1, 3, 4, 8, 11, 6, -5, -7, -3, 9, 7, 0, -4, -6, 2])))
    print("{} == 61".format(contigsum([7, -1, 8, 0, 5, 1, 10, 2, -7, 3, -5, 11, 12, -4, 9, 6, 4, -3, -2, -6])))
