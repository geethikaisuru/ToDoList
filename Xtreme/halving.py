from collections import defaultdict

MOD = 998244353


def solve():
    N = int(input())
    C = list(map(int, input().split()))
    R = list(map(int, input().split()))
    B = list(map(int, input().split()))

    b_pos = {b: i for i, b in enumerate(B)}

    fixedPos = {}
    fixedNs = set()
    unkPos = []

    for g, num in enumerate(C):
        if num != -1:
            fixedPos[num] = g
            fixedNs.add(num)
        else:
            unkPos.append(g)


    for g in range(N):
        pos1, pos2 = 2 * g, 2 * g + 1
        b = B[g]



        if C[pos1] != -1 and C[pos2] != -1:
            if R[g] == 0 and min(C[pos1], C[pos2]) != b:
                return 0
            if R[g] == 1 and max(C[pos1], C[pos2]) != b:
                return 0

        elif C[pos1] != -1:
            if R[g] == 0 and C[pos1] < b:
                return 0
            if R[g] == 1 and C[pos1] > b:
                return 0
        elif C[pos2] != -1:
            if R[g] == 0 and C[pos2] < b:
                return 0
            if R[g] == 1 and C[pos2] > b:
                return 0
    dp = defaultdict(int)
    dp[0] = 1

    def get_bit(mask, pos):
        return (mask >> pos) & 1

    def set_bit(mask, pos):
        return mask | (1 << pos)
    for g in range(N):
        pos1, pos2 = 2 * g, 2 * g + 1
        b = B[g]
        newDP = defaultdict(int)


        for mask in dp:
            count = dp[mask]
            if count == 0:
                continue
            for n1 in range(1, 2 * N + 1):
                if n1 in fixedNs:
                    if fixedPos[n1] not in (pos1, pos2):
                        continue
                elif get_bit(mask, n1 - 1):
                    continue

                for n2 in range(1, 2 * N + 1):
                    if n1 == n2:
                        continue
                    if n2 in fixedNs:
                        if fixedPos[n2] not in (pos1, pos2):
                            continue
                    elif get_bit(mask, n2 - 1):
                        continue

                    if R[g] == 0 and min(n1, n2) != b:
                        continue
                    if R[g] == 1 and max(n1, n2) != b:
                        continue


                    if n1 in fixedNs and fixedPos[n1] == pos2:
                        continue
                    if n2 in fixedNs and fixedPos[n2] == pos1:
                        continue



                    new_mask = set_bit(set_bit(mask, n1 - 1), n2 - 1)
                    newDP[new_mask] = (newDP[new_mask] + count) % MOD

        dp = newDP
    result = sum(dp.values()) % MOD
    return result


print(solve())