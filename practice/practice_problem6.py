from typing import List


def maxDistToClosest(seats: List[int]) -> int:
    cur, n = 0, len(seats)
    for k in range(n):
        if seats[k]:
            break
        else:
            cur += 1
    res = cur
    zeros = cur = 0
    for i in range(k, n):
        if seats[i]:
            zeros = max(zeros, cur)
            cur = 0
        else:
            cur += 1
    res = max(res, (zeros + 1) // 2, cur)
    return res

seats = [1,0,0,0,1,0,1]
seat = [1,0,0,0]
seatz = [1,0]
print(maxDistToClosest(seats))
print(maxDistToClosest(seat))
print(maxDistToClosest(seatz))